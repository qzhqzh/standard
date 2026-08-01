# Architecture

Repo Standard is both a reference repository and a dependency-free Python CLI.

```text
CLI
  ├── logging configuration and redaction
  ├── policy loader/validator
  └── repository checker
        └── immutable rule/result models
```

## Data flow

1. CLI resolves arguments and stderr logging.
2. Policy loader reads UTF-8 TOML and validates schema, levels, modes, unique IDs, and safe relative patterns.
3. Checker resolves the root, evaluates exact paths/globs, and computes a weighted score.
4. Renderer emits text or versioned JSON to stdout.
5. Exit codes: `0` accepted, `2` policy failure, `1` operational/configuration error.

## Trust boundaries

The scanned repository is untrusted. The checker reads path metadata but never imports, executes, or parses target source. Policies cannot use absolute or `..` paths. Logs may be public in CI. Actions are privileged and therefore least-privilege and SHA-pinned.

## Compatibility and extensions

Python 3.11+ is supported. JSON output has `schema_version = 1`; rule IDs should remain stable. Future extensions may add semantic checks, profiles, OSPS mappings, SARIF, GitHub settings checks, and remediation patches while keeping the offline core safe.

The checker does not prove content quality, license correctness, vulnerability absence, or server-side setting enforcement.
