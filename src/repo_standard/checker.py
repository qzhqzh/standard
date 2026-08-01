from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from repo_standard.models import Level, Policy, Rule, RuleResult

_LEVEL_WEIGHT = {
    Level.REQUIRED: 5,
    Level.RECOMMENDED: 2,
    Level.OPTIONAL: 1,
}


@dataclass(frozen=True, slots=True)
class ScanReport:
    root: Path
    policy_name: str
    results: tuple[RuleResult, ...]
    score: int

    @property
    def failed(self) -> tuple[RuleResult, ...]:
        return tuple(result for result in self.results if not result.passed)

    def counts(self) -> dict[str, dict[str, int]]:
        totals = Counter(result.rule.level.value for result in self.results)
        passed = Counter(result.rule.level.value for result in self.results if result.passed)
        return {
            level.value: {"passed": passed[level.value], "total": totals[level.value]}
            for level in Level
        }


def _matches(root: Path, pattern: str) -> tuple[str, ...]:
    if any(character in pattern for character in "*?["):
        candidates = root.glob(pattern)
    else:
        candidate = root / pattern
        candidates = (candidate,) if candidate.exists() else ()

    relative: list[str] = []
    for candidate in candidates:
        try:
            relative.append(candidate.relative_to(root).as_posix())
        except ValueError:
            continue
    return tuple(sorted(set(relative)))


def _evaluate_rule(root: Path, rule: Rule) -> RuleResult:
    pattern_matches = {pattern: _matches(root, pattern) for pattern in rule.paths}
    passed = (
        all(pattern_matches[pattern] for pattern in rule.paths)
        if rule.mode == "all"
        else any(pattern_matches[pattern] for pattern in rule.paths)
    )
    matched = tuple(path for pattern in rule.paths for path in pattern_matches[pattern])
    missing = tuple(pattern for pattern in rule.paths if not pattern_matches[pattern])
    return RuleResult(
        rule=rule,
        passed=passed,
        matched_paths=tuple(sorted(set(matched))),
        missing_patterns=missing,
    )


def _score(results: tuple[RuleResult, ...]) -> int:
    possible = sum(_LEVEL_WEIGHT[result.rule.level] for result in results)
    earned = sum(_LEVEL_WEIGHT[result.rule.level] for result in results if result.passed)
    return round((earned / possible) * 100) if possible else 100


def scan_repository(root: Path, policy: Policy) -> ScanReport:
    """Evaluate a repository root against a validated policy."""

    resolved = root.expanduser().resolve()
    if not resolved.exists():
        raise FileNotFoundError(f"repository path does not exist: {resolved}")
    if not resolved.is_dir():
        raise NotADirectoryError(f"repository path is not a directory: {resolved}")

    results = tuple(_evaluate_rule(resolved, rule) for rule in policy.rules)
    return ScanReport(
        root=resolved,
        policy_name=policy.name,
        results=results,
        score=_score(results),
    )
