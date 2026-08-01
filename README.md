# Repo Standard

[![CI](https://github.com/qzhqzh/standard/actions/workflows/ci.yml/badge.svg)](https://github.com/qzhqzh/standard/actions/workflows/ci.yml)
[![CodeQL](https://github.com/qzhqzh/standard/actions/workflows/codeql.yml/badge.svg)](https://github.com/qzhqzh/standard/actions/workflows/codeql.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/qzhqzh/standard/badge)](https://scorecard.dev/viewer/?uri=github.com/qzhqzh/standard)
[![Latest release](https://img.shields.io/github/v/release/qzhqzh/standard?sort=semver)](https://github.com/qzhqzh/standard/releases)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/github/license/qzhqzh/standard)](LICENSE)

**Repo Standard** is a runnable, security-conscious reference repository for building consistent open-source projects. It also ships a small CLI that checks another repository against the same policy.

[简体中文](README.zh-CN.md) · [Open-source standard](docs/OPEN_SOURCE_STANDARD.md) · [Adoption checklist](docs/ADOPTION_CHECKLIST.md) · [Repository settings](docs/REPOSITORY_SETTINGS.md)

## Why this repository exists

A serious open-source project is more than source code. Users need to understand it, contributors need a predictable workflow, maintainers need operational boundaries, and downstream consumers need evidence that releases are built and governed responsibly.

This repository demonstrates:

- clear identity, installation, usage, compatibility, support, and lifecycle documentation;
- license, contribution rules, governance, code of conduct, maintainers, and citation metadata;
- tests, formatting, type checking, build validation, structured logging, and architecture records;
- coordinated vulnerability disclosure, dependency updates, CodeQL, dependency review, OpenSSF Scorecard, least-privilege workflows, and immutable action pins;
- Semantic Versioning, a human-maintained changelog, release artifacts, and build provenance attestations.

## Quick start

Requires Python 3.11 or newer. The checker itself has no runtime dependencies.

```bash
git clone https://github.com/qzhqzh/standard.git
cd standard
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -e .
repo-standard check .
```

Check another repository:

```bash
repo-standard check ../my-project
repo-standard check ../my-project --format json
repo-standard check ../my-project --fail-level recommended
repo-standard check ../my-project --policy ./standard.toml
```

Example output:

```text
Repo Standard report: /work/my-project
Score: 88/100

PASS  required     README and project identity
PASS  required     Open-source license
FAIL  recommended  Coordinated dependency updates
      Configure Dependabot or Renovate.
```

## The standard at a glance

| Area | Baseline | Mature-project extension |
| --- | --- | --- |
| Identity | README, examples, compatibility, status | bilingual docs, branding guide, roadmap |
| Legal | explicit OSI license | NOTICE, SPDX/REUSE, citation, trademark policy |
| Community | CONTRIBUTING, Code of Conduct, support path | governance, maintainers, succession, discussions |
| Quality | tests and CI | formatting, typing, coverage policy, ADRs |
| Security | SECURITY.md, private reporting, dependency updates | CodeQL, dependency review, Scorecard, threat model |
| Supply chain | least-privilege CI and pinned actions | artifact attestations, SBOM, trusted publishing |
| Operations | documented log levels and secret redaction | JSON logs, correlation IDs, audit-log separation |
| Releases | SemVer and changelog | reproducible artifacts, provenance, release checklist |

The normative MUST/SHOULD/MAY matrix is in [`docs/OPEN_SOURCE_STANDARD.md`](docs/OPEN_SOURCE_STANDARD.md).

## Use this as your project template

1. Copy the community, security, workflow, and documentation files that match your project type.
2. Replace repository names, package names, owners, support channels, and release targets.
3. Delete irrelevant examples rather than leaving misleading placeholders.
4. Apply the server-side settings in [`docs/REPOSITORY_SETTINGS.md`](docs/REPOSITORY_SETTINGS.md).
5. Run `repo-standard check . --fail-level recommended` in CI and tighten the policy as the project matures.

## Development

```bash
python -m pip install -e '.[dev]'
make check
make test
make build
```

## Security, support, and contribution

Do not report vulnerabilities in public issues. Follow [`SECURITY.md`](SECURITY.md). Read [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SUPPORT.md`](SUPPORT.md), and [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) before participating.

## Project status

The reference implementation is intentionally small and stable. The policy and documentation will evolve as GitHub, OpenSSF, language ecosystems, and supply-chain practices change.

## License

Licensed under the [Apache License 2.0](LICENSE). See [`NOTICE`](NOTICE).
