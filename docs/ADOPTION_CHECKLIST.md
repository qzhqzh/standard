# Adoption checklist

Bring an existing repository to the standard in reviewable stages.

## 1. Make it understandable and legal

- [ ] Confirm name, description, audience, status, and supported versions.
- [ ] Rewrite README around purpose, quick start, minimal example, support, security, contribution, and license.
- [ ] Select an appropriate license; obtain legal review when ownership is unclear.
- [ ] Reconcile NOTICE and third-party attributions.
- [ ] Remove committed secrets and rotate them before making the repository public.

## 2. Establish contribution and security boundaries

- [ ] Add CONTRIBUTING, Code of Conduct, SECURITY, and SUPPORT.
- [ ] Enable private vulnerability reporting.
- [ ] Add bug/feature forms and a pull-request template.
- [ ] Add maintainers, governance, CODEOWNERS, and sensitive-path ownership.
- [ ] Define non-goals and unsupported use.

## 3. Make quality executable

- [ ] Add the canonical manifest and supported runtime versions.
- [ ] Add deterministic commands for format, lint, typing, tests, and build.
- [ ] Add least-privilege CI with timeouts and concurrency.
- [ ] Add a lockfile or dependency-resolution policy appropriate to the ecosystem.
- [ ] Install/run the built artifact, not only source tests.

## 4. Add automated security

- [ ] Enable dependency graph, Dependabot alerts/security updates/version updates, secret scanning, and push protection.
- [ ] Add dependency review, CodeQL/equivalent SAST, and OpenSSF Scorecard.
- [ ] Pin actions to full SHAs and update them with Dependabot.
- [ ] Add a threat model and tests for highest-risk abuse cases.
- [ ] Configure a default-branch ruleset with reviews and required checks.

## 5. Make releases trustworthy

- [ ] Adopt versioning and changelog conventions.
- [ ] Document preparation, approval, build, publication, verification, and rollback.
- [ ] Publish from a protected workflow/environment, not a laptop.
- [ ] Generate provenance attestations.
- [ ] Add an SBOM and trusted publishing when consumers or regulation justify them.

## 6. Enforce progressively

```bash
repo-standard check . --format json > repo-standard-report.json
repo-standard check . --fail-level required
```

Start by blocking required failures. Move to `recommended` only after the team accepts the maintenance cost.
