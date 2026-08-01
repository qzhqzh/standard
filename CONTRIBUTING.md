# Contributing

Thank you for improving Repo Standard. Contributions should make the reference easier to adopt, safer to operate, or more precise across project types.

## Before opening work

- Search existing issues and pull requests.
- Use an issue for changes that alter policy semantics, compatibility, security posture, licensing, or governance.
- Never include credentials, private incident details, customer data, or embargoed vulnerability information.

## Development setup

```bash
git clone https://github.com/qzhqzh/standard.git
cd standard
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -e '.[dev]'
make check
```

Runtime code should remain dependency-free unless a dependency has a clear security and maintenance justification.

## Branches and commits

Use focused branches such as `feat/policy-rule` or `docs/release-guidance`. Commit messages follow Conventional Commits:

```text
feat(policy): detect missing private-reporting guidance
fix(cli): return required-rule failure code
docs: clarify release verification
```

Common types are `feat`, `fix`, `docs`, `test`, `refactor`, `build`, `ci`, `chore`, and `security`. Mark incompatible changes with `!` or a `BREAKING CHANGE:` footer.

## Pull requests

A pull request should explain the problem and approach, stay focused, include tests, update affected docs or threat models, and pass formatting, lint, typing, tests, build, dependency review, and security checks. Do not weaken workflow permissions or replace immutable action SHAs with mutable tags.

Policy changes must include a stable ID, level, machine-checkable patterns, rationale, remediation, and matching changes in both policy files.

## Security reports

Do not disclose suspected vulnerabilities in an issue or pull request. Follow [`SECURITY.md`](SECURITY.md).

## Review and licensing

Maintainers use squash merge. Non-trivial changes require review. By contributing, you agree that your contribution is licensed under Apache-2.0.
