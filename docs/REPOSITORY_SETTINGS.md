# GitHub repository settings

Files provide guidance; GitHub settings enforce it.

## Identity and merge behavior

- Add a concise description, homepage/docs link, topics, and social preview.
- Enable Issues/Discussions only when maintainers can support them.
- Prefer squash merge for a compact Conventional-Commit-compatible history.
- Automatically delete merged branches.

## Access control

- Require MFA; prefer passkeys or hardware-backed factors.
- Grant minimum roles and separate triage, write, admin, security, and release authority.
- Review collaborators, deploy keys, GitHub Apps, tokens, and dormant maintainers quarterly.
- Prefer OIDC trusted publishing over long-lived registry/cloud tokens.

## Default-branch ruleset

Target `main` and require:

- pull requests before merge;
- at least one approval, two for high-impact/security paths when staffing permits;
- stale approval dismissal after new commits;
- CODEOWNERS review;
- resolved conversations;
- CI, tests, build, dependency review, and CodeQL checks;
- no force push or deletion;
- linear history when using squash/rebase;
- narrowly controlled and audited bypass.

Use a separate tag ruleset for `v*`; prevent published tag update/deletion.

## Actions

- Set default `GITHUB_TOKEN` to read-only.
- Allow only GitHub-authored, verified, or explicitly approved actions.
- Require full-length action SHAs.
- Require approval for first-time/untrusted fork workflows.
- Never run arbitrary public-fork code on privileged self-hosted runners.

## Security features

Enable dependency graph, Dependabot alerts, security updates, version updates, secret scanning, push protection, CodeQL, private vulnerability reporting, and security advisories.

## Releases

Create a protected `release` or `pypi` environment. Restrict deployment sources, require review, use OIDC, never expose release credentials to PR workflows, retain provenance, and verify published artifacts independently.
