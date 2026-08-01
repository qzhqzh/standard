from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Literal


class Level(StrEnum):
    REQUIRED = "required"
    RECOMMENDED = "recommended"
    OPTIONAL = "optional"


@dataclass(frozen=True, slots=True)
class Rule:
    id: str
    title: str
    level: Level
    mode: Literal["any", "all"]
    paths: tuple[str, ...]
    rationale: str
    remediation: str


@dataclass(frozen=True, slots=True)
class Policy:
    schema_version: int
    name: str
    rules: tuple[Rule, ...]


@dataclass(frozen=True, slots=True)
class RuleResult:
    rule: Rule
    passed: bool
    matched_paths: tuple[str, ...]
    missing_patterns: tuple[str, ...]
