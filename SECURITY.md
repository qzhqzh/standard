# Security Policy

## Supported versions

| Version | Supported |
| --- | --- |
| Latest minor release | Yes |
| Previous minor release | Security fixes when practical |
| Older releases | No |

Before 1.0, security fixes may be released only on the latest version.

## Report a vulnerability privately

Do **not** open a public issue, discussion, or pull request. Use the repository's **Security → Report a vulnerability** flow.

Include the affected version or commit, component, attack preconditions, reproduction steps or a minimal proof of concept, realistic impact, and suggested mitigation. Use synthetic data; never include real credentials, personal data, destructive payloads, or third-party secrets.

## Response targets

The project aims to acknowledge a complete report within 3 business days, provide an initial assessment within 7 business days, and communicate progress at least every 14 days while active. These are targets, not guarantees.

## Coordinated disclosure

Maintainers validate the report, assign severity, develop and test a fix, prepare an advisory, and coordinate disclosure. Credit is offered unless anonymity is requested or testing violated this policy.

## Safe-harbor expectations

Good-faith research must avoid privacy violations, disruption, data destruction, persistence, social engineering, and access beyond what is necessary to demonstrate impact. Stop testing if sensitive data or other users are affected.

See [`docs/THREAT_MODEL.md`](docs/THREAT_MODEL.md), [`docs/SECURITY_HARDENING.md`](docs/SECURITY_HARDENING.md), and [`docs/RELEASE_PROCESS.md`](docs/RELEASE_PROCESS.md).
