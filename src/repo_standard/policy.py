from __future__ import annotations

import tomllib
from importlib.resources import files
from pathlib import Path
from typing import Any, Literal, cast

from repo_standard.models import Level, Policy, Rule

SUPPORTED_SCHEMA_VERSION = 1


class PolicyError(ValueError):
    """Raised when a policy file is malformed or unsafe."""


def _required_string(data: dict[str, Any], key: str, context: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise PolicyError(f"{context}.{key} must be a non-empty string")
    return value.strip()


def _validate_pattern(pattern: str, context: str) -> str:
    path = Path(pattern)
    if path.is_absolute() or ".." in path.parts:
        raise PolicyError(f"{context} contains unsafe path pattern: {pattern!r}")
    return pattern


def _parse_rule(raw: object, index: int) -> Rule:
    context = f"rules[{index}]"
    if not isinstance(raw, dict):
        raise PolicyError(f"{context} must be a table")
    data = cast(dict[str, Any], raw)

    raw_paths = data.get("paths")
    if not isinstance(raw_paths, list) or not raw_paths:
        raise PolicyError(f"{context}.paths must be a non-empty array")
    paths: list[str] = []
    for value in raw_paths:
        if not isinstance(value, str) or not value.strip():
            raise PolicyError(f"{context}.paths must contain non-empty strings")
        paths.append(_validate_pattern(value.strip(), context))

    raw_level = _required_string(data, "level", context)
    try:
        level = Level(raw_level)
    except ValueError as exc:
        raise PolicyError(f"{context}.level is invalid: {raw_level!r}") from exc

    raw_mode = _required_string(data, "mode", context)
    if raw_mode not in {"any", "all"}:
        raise PolicyError(f"{context}.mode must be 'any' or 'all'")

    return Rule(
        id=_required_string(data, "id", context),
        title=_required_string(data, "title", context),
        level=level,
        mode=cast(Literal["any", "all"], raw_mode),
        paths=tuple(paths),
        rationale=_required_string(data, "rationale", context),
        remediation=_required_string(data, "remediation", context),
    )


def load_policy(path: Path | None = None) -> Policy:
    """Load and validate a policy from disk or the packaged default."""

    if path is None:
        content = files("repo_standard").joinpath("default_policy.toml").read_text(encoding="utf-8")
        source = "packaged default policy"
    else:
        try:
            content = path.read_text(encoding="utf-8")
        except OSError as exc:
            raise PolicyError(f"could not read policy {path}: {exc}") from exc
        source = str(path)

    try:
        raw = tomllib.loads(content)
    except tomllib.TOMLDecodeError as exc:
        raise PolicyError(f"invalid TOML in {source}: {exc}") from exc

    schema_version = raw.get("schema_version")
    if schema_version != SUPPORTED_SCHEMA_VERSION:
        raise PolicyError(
            f"unsupported schema_version {schema_version!r}; expected {SUPPORTED_SCHEMA_VERSION}"
        )

    name = raw.get("name")
    if not isinstance(name, str) or not name.strip():
        raise PolicyError("policy name must be a non-empty string")

    raw_rules = raw.get("rules")
    if not isinstance(raw_rules, list) or not raw_rules:
        raise PolicyError("policy must contain at least one [[rules]] table")

    rules = tuple(_parse_rule(raw_rule, index) for index, raw_rule in enumerate(raw_rules))
    ids = [rule.id for rule in rules]
    if len(ids) != len(set(ids)):
        raise PolicyError("rule ids must be unique")

    return Policy(schema_version=schema_version, name=name.strip(), rules=rules)
