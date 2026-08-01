# ADR 0001: Use a declarative TOML policy

- **Status:** Accepted
- **Date:** 2026-08-01

## Context

The reference must work across languages and allow policy evolution without rewriting scanner logic. Executable plugins would create unnecessary risk.

## Decision

Rules are TOML data with stable IDs, levels, relative path patterns, match mode, rationale, and remediation. The scanner supports exact paths and globs, rejects absolute/parent traversal, and never executes target code.

## Alternatives

Hard-coded Python couples policy and releases. YAML needs a third-party parser. Executable plugins are expressive but unsafe. A full content policy language is too complex for the first baseline.

## Consequences

The core remains dependency-free and offline. Policy changes are reviewable. Presence cannot prove content quality, so results are evidence prompts rather than certification.
