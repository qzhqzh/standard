# Release process

Repo Standard follows Semantic Versioning. Before 1.0, breaking behavior still requires prominent notes.

## Prepare

1. Confirm CI, CodeQL, dependency review, and Scorecard health.
2. Resolve or explicitly accept relevant security alerts.
3. Update changelog, compatibility, supported versions, and migration guidance.
4. Set the version consistently in package and citation metadata.
5. Build and install the wheel in a clean environment.
6. Review the final diff and obtain approval.

## Release

```bash
git switch main
git pull --ff-only
git tag -s v0.1.0 -m "repo-standard v0.1.0"
git push origin v0.1.0
```

The tag workflow tests, builds, attests distributions, uploads artifacts, and creates a GitHub Release.

## Verify

```bash
gh release download v0.1.0 -R qzhqzh/standard
gh attestation verify repo_standard-0.1.0-py3-none-any.whl -R qzhqzh/standard
```

Install the wheel in a clean environment and run it. Verify notes, names, license inclusion, and changelog links.

## Registry publication

This reference does not publish to PyPI automatically. To add it, create a protected environment, configure exact-repository trusted publishing, pin the official publish action by full SHA, and avoid long-lived tokens.

## Emergency and rollback

Use private advisory work, limit disclosure, release the fix before/with disclosure, rotate credentials, and notify downstreams. Never silently replace artifacts or move tags. Publish a corrected version, mark the bad release withdrawn, and delete invalid attestations when consumers must stop trusting an artifact.
