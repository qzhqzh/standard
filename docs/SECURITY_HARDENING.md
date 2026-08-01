# Security hardening guide

## Dependencies

Avoid unnecessary dependencies. Verify authentic upstream ownership, maintenance, license, security policy, install scripts, and transitive risk. Separate runtime and development dependencies. Applications should use reproducible lockfiles; libraries should declare compatible ranges and test supported versions.

## Secrets

Never commit secrets. Use OIDC short-lived credentials, protected environments, and narrow scope. Treat logs, fixtures, screenshots, workflow artifacts, and crash dumps as secret channels. Rotate exposed credentials immediately; deleting a commit is insufficient.

## Actions

Every workflow should declare permissions, pin actions to full SHAs, set `persist-credentials: false` unless pushing is required, use timeouts/concurrency, avoid shell interpolation of untrusted GitHub context, and separate untrusted validation from privileged release/deployment jobs.

Avoid `pull_request_target` unless attacker-controlled content is never executed or sourced.

## Analysis and tests

Use SAST, dependency review, secret scanning, and tests for authorization, validation, path handling, serialization, command execution, and unsafe file formats. Add fuzzing at parsers/protocol boundaries.

## Releases

Build reviewed source in a protected workflow. Publish hashes/provenance and, where justified, an SBOM. Attestation proves origin and build context, not vulnerability absence.

## Incident readiness

Maintain private reporting, response roles, severity criteria, release authority, downstream notification, credential rotation, and advisory procedures. Exercise the process before a real incident.
