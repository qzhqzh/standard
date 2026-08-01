# Threat model

## Assets

Policy integrity, private vulnerability reports, release credentials, artifact provenance, maintainer access, and user trust.

## Actors and entry points

Malformed or malicious repositories/policies, compromised dependencies/actions, compromised maintainers, control-weakening contributions, public disclosure attempts, CLI paths, TOML, pull requests, tags, logs, artifacts, and attachments.

## Threats and mitigations

| Threat | Mitigation |
| --- | --- |
| Target repository executes code | Scanner checks path metadata only. |
| Policy escapes repository root | Reject absolute and `..` patterns; report relative matches. |
| Secrets leak in logs | Separate streams, allowlisted fields, redaction, sanitization guidance. |
| Action supply-chain compromise | SHA pins, least privilege, Dependabot, Scorecard, protected releases. |
| PR gains release credentials | PR workflows have no release secrets; releases use protected tags/OIDC. |
| Maintainer account compromise | MFA, tag/environment protection, review, attestations, access review. |
| Badge/score is mistaken for proof | Docs explicitly describe evidence limits. |
| Public vulnerability harms users | SECURITY.md directs private coordinated disclosure. |

## Residual risk

The scanner validates presence, not semantic correctness. Empty or misleading files can pass. GitHub settings require separate review.

Update this model when adding content parsing, network/API access, automatic patches, archive extraction, plugins, credentials, publication, or self-hosted runners.
