from __future__ import annotations

import argparse
import json
import logging
from collections.abc import Sequence
from pathlib import Path

from repo_standard.checker import ScanReport, scan_repository
from repo_standard.logging_config import configure_logging
from repo_standard.policy import PolicyError, load_policy

LOGGER = logging.getLogger("repo_standard")
_LEVEL_ORDER = {"required": 0, "recommended": 1, "optional": 2, "never": 99}


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="repo-standard",
        description="Check a repository against a healthy open-source project policy.",
    )
    subparsers = parser.add_subparsers(dest="command")
    check = subparsers.add_parser("check", help="scan a repository")
    check.add_argument("path", nargs="?", default=".", type=Path)
    check.add_argument("--policy", type=Path, help="TOML policy; packaged policy is the default")
    check.add_argument("--format", choices=("text", "json"), default="text", dest="output_format")
    check.add_argument(
        "--fail-level",
        choices=("required", "recommended", "optional", "never"),
        default="required",
        help="lowest missing level that returns exit code 2",
    )
    check.add_argument("--log-format", choices=("text", "json"), default="text")
    check.add_argument("--verbose", action="store_true")
    return parser


def _as_dict(report: ScanReport) -> dict[str, object]:
    return {
        "schema_version": 1,
        "repository": str(report.root),
        "policy": report.policy_name,
        "score": report.score,
        "counts": report.counts(),
        "results": [
            {
                "id": result.rule.id,
                "title": result.rule.title,
                "level": result.rule.level.value,
                "passed": result.passed,
                "matched_paths": list(result.matched_paths),
                "missing_patterns": list(result.missing_patterns),
                "rationale": result.rule.rationale,
                "remediation": result.rule.remediation,
            }
            for result in report.results
        ],
    }


def _print_text(report: ScanReport) -> None:
    print(f"Repo Standard report: {report.root}")
    print(f"Policy: {report.policy_name}")
    print(f"Score: {report.score}/100\n")
    for result in report.results:
        status = "PASS" if result.passed else "FAIL"
        print(f"{status:<5} {result.rule.level.value:<11} {result.rule.title}")
        if not result.passed:
            print(f"      {result.rule.remediation}")
    counts = report.counts()
    print()
    print(
        "  ".join(
            f"{level.title()}: {counts[level]['passed']}/{counts[level]['total']}"
            for level in ("required", "recommended", "optional")
        )
    )


def _should_fail(report: ScanReport, fail_level: str) -> bool:
    if fail_level == "never":
        return False
    threshold = _LEVEL_ORDER[fail_level]
    return any(
        not result.passed and _LEVEL_ORDER[result.rule.level.value] <= threshold
        for result in report.results
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    if args.command is None:
        args = parser.parse_args(["check", *(argv or [])])

    configure_logging(verbose=args.verbose, json_logs=args.log_format == "json")

    try:
        policy = load_policy(args.policy)
        report = scan_repository(args.path, policy)
    except (PolicyError, OSError, ValueError) as exc:
        LOGGER.error("scan_failed: %s", exc, extra={"event": "scan_failed"})
        return 1

    LOGGER.info(
        "scan_complete",
        extra={
            "event": "scan_complete",
            "repository": str(report.root),
            "score": report.score,
            "failed_rules": len(report.failed),
        },
    )

    if args.output_format == "json":
        print(json.dumps(_as_dict(report), ensure_ascii=False, indent=2))
    else:
        _print_text(report)

    return 2 if _should_fail(report, args.fail_level) else 0
