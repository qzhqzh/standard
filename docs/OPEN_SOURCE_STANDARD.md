# Open-source project standard

This is the normative guide behind Repo Standard. **MUST** means a public project is materially incomplete without the practice. **SHOULD** means it is expected unless a documented reason makes it inappropriate. **MAY** means it is valuable for particular project types or maturity levels.

## Principles

1. **Users first:** a visitor should understand value, status, installation, and the first successful example quickly.
2. **Explicit over tribal knowledge:** contribution, support, security, release, and governance rules belong in versioned files.
3. **Evidence over claims:** tests, CI, scans, and provenance are stronger than adjectives or badges.
4. **Least privilege:** automation receives only the permissions and secrets needed for one job.
5. **Portable records:** important history must not exist only in a vendor dashboard or chat.
6. **Progressive maturity:** small projects need a strong baseline, not copied enterprise ceremony.
7. **No misleading placeholders:** delete inactive contacts, badges, funding links, and workflows.

## Normative matrix

### Identity and README

| Level | Requirement |
| --- | --- |
| MUST | State name, one-sentence purpose, maturity/status, supported platforms/versions, installation, minimal usage, license, contribution, support, and security links. |
| MUST | Show the shortest tested path to a successful result. |
| SHOULD | Explain core features, non-goals, compatibility, architecture entry points, and upgrades. |
| SHOULD | Keep screenshots, benchmarks, and claims current and reproducible. |
| MAY | Maintain localized entry documentation when it can be kept synchronized. |

A README is an entry point, not the whole manual. Move operational detail to `docs/` and keep stable links.

### Legal, licensing, attribution, and “certificates”

| Level | Requirement |
| --- | --- |
| MUST | Include the full canonical text of an explicit OSI-approved license before calling the repository open source. |
| MUST | Ensure inbound contribution terms are compatible with the outbound license. |
| SHOULD | Add SPDX identifiers or adopt REUSE when license composition is complex. |
| SHOULD | Preserve required third-party notices and license files. |
| MAY | Add `CITATION.cff` for research-facing or widely cited software. |
| MAY | Register for OpenSSF Best Practices only after the underlying practices are real. |

A license grants legal permissions. A badge or certification signals assessed practices. A signed or attested release proves origin. None proves that software has no vulnerabilities.

### Community and contribution

| Level | Requirement |
| --- | --- |
| MUST | Add CONTRIBUTING with setup, validation, scope, commits, pull requests, review, and security handling. |
| MUST | Add and enforce a Code of Conduct with a private reporting route. |
| MUST | Separate security reports from public bug reports. |
| SHOULD | Add structured bug and feature issue forms. |
| SHOULD | Add a pull-request template covering tests, risk, compatibility, security, docs, and release impact. |
| SHOULD | Publish support routes and boundaries. |
| MAY | Enable Discussions, funding, translations, or good-first-issue programs when maintainers can support them. |

### Governance and ownership

| Level | Requirement |
| --- | --- |
| SHOULD | Publish maintainers, roles, decision process, admission/removal criteria, security authority, and succession. |
| SHOULD | Use CODEOWNERS for sensitive paths and enforce it with a ruleset. |
| SHOULD | Record material compatibility, security, licensing, data, or architecture decisions as ADRs. |
| MAY | Add RFCs, working groups, steering committees, or formal voting as contributor count grows. |

CODEOWNERS is review routing, not a complete governance or access-control model.

### Engineering quality

| Level | Requirement |
| --- | --- |
| MUST | Use the ecosystem's canonical manifest and declare supported runtime versions. |
| MUST | Provide automated tests and a documented local command. |
| MUST | Run CI on pull requests and the default branch. |
| SHOULD | Enforce deterministic formatting, linting, typing where supported, and build/install validation. |
| SHOULD | Define compatibility and deprecation for public APIs. |
| MAY | Add coverage thresholds, benchmarks, fuzzing, mutation testing, and platform matrices when they protect real risks. |

Coverage percentage is not a substitute for meaningful assertions and boundary cases.

### Security and vulnerability management

| Level | Requirement |
| --- | --- |
| MUST | Publish supported versions, a private reporting route, expected report contents, and coordinated disclosure. |
| MUST | Prevent secrets from entering source; public repositories should enable secret scanning and push protection. |
| MUST | Protect the default branch from force pushes and unreviewed direct changes. |
| SHOULD | Enable the dependency graph, Dependabot alerts, security updates, and scheduled version updates. |
| SHOULD | Run dependency review and a language-aware scanner such as CodeQL. |
| SHOULD | Maintain a threat model for externally reachable, privileged, or data-processing software. |
| SHOULD | Run OpenSSF Scorecard and treat findings as leads, not a certificate. |
| MAY | Add fuzzing, penetration tests, external audits, or a bug bounty when risk and adoption justify them. |

### GitHub Actions and supply-chain security

| Level | Requirement |
| --- | --- |
| MUST | Declare explicit workflow/job permissions; default to read-only. |
| MUST | Never expose trusted secrets to untrusted pull-request code. Avoid `pull_request_target` with attacker-controlled checkout/build. |
| SHOULD | Pin every external action to a full commit SHA and retain a readable version comment. |
| SHOULD | Set timeouts, concurrency, minimal checkout credentials, and narrow environment access. |
| SHOULD | Update action pins automatically and review action ownership. |
| SHOULD | Build releases in protected workflows and generate provenance attestations for consumer-facing artifacts. |
| MAY | Generate/attest an SBOM, use SLSA-compatible builders, and verify provenance at deployment. |

A tag such as `@v4` is convenient but mutable. A full SHA is the immutable action reference GitHub recommends.

### Logging and observability

| Level | Requirement |
| --- | --- |
| MUST | Never log credentials, tokens, private keys, authorization headers, or raw sensitive payloads. |
| SHOULD | Define stable DEBUG/INFO/WARNING/ERROR/CRITICAL semantics. |
| SHOULD | Emit structured production logs with timestamp, level, event, component, version, and correlation ID where applicable. |
| SHOULD | Separate audit events from diagnostic logs and define retention/access. |
| SHOULD | Sanitize logs before attaching them to issues. |
| MAY | Add traces, metrics, error aggregation, and service objectives for deployed services. |

### Versioning, changelog, and release

| Level | Requirement |
| --- | --- |
| MUST | Define version meaning; public libraries should normally use Semantic Versioning. |
| SHOULD | Maintain `CHANGELOG.md` with an Unreleased section and one dated entry per release. |
| SHOULD | Use Conventional Commits or another documented intent convention. |
| SHOULD | Release from reviewed default-branch code and publish verification evidence. |
| SHOULD | Document rollback, yanking, revocation, and emergency security releases. |
| MAY | Automate release notes, OIDC trusted publishing, SBOMs, provenance, and downstream compatibility tests. |

Release notes market one release. A changelog is the durable human history.

### Badges and branding

| Level | Requirement |
| --- | --- |
| MUST | Every badge links to evidence and reflects a maintained process. Remove broken or misleading badges. |
| SHOULD | Limit the first row to CI, security/Scorecard, release, runtime compatibility, and license. |
| SHOULD | Use accessible alt text and avoid color-only meaning. |
| MAY | Add logos, screenshots, social preview, trademark guidance, and brand assets for a stable identity. |

## Maturity profiles

**Baseline:** all MUST items, one maintainer, CI, private vulnerability reporting, dependency alerts, and explicit experimental status.

**Maintained:** add all SHOULD items—structured intake, ownership, dependency updates, scanning, changelog, release process, architecture, logging policy, and rulesets.

**Critical/widely consumed:** add multiple maintainers, protected releases, provenance, SBOM, external assessment/fuzzing, succession, compatibility tests, and OpenSSF baseline/badge work.

## What files cannot enforce

Server-side settings still matter: MFA, collaborator roles, rulesets, private vulnerability reporting, secret scanning/push protection, dependency alerts, action policies, protected environments, and immutable releases. Apply [`REPOSITORY_SETTINGS.md`](REPOSITORY_SETTINGS.md).

## Review cadence

- Every release: changelog, compatibility, supported versions, artifacts, provenance, and release notes.
- Monthly: dependency/security alerts, failing workflows, access changes, and open security reports.
- Quarterly: maintainers, governance, roadmap, actions, threat model, rulesets, and docs accuracy.
- Annually: license/notice inventory, incident exercise, succession, links, and OpenSSF assessment.
