# Logging standard

Logs are an operational interface. They must support diagnosis without leaking secrets or creating unnecessary personal-data retention.

## Destinations

- Reports and command output: stdout.
- Diagnostics and lifecycle logs: stderr.
- Production services: structured JSON.
- Security audit events: distinct sink, schema, access policy, and retention.

## Structured fields

Use UTC timestamp, level, stable event name, component/logger, short message, software version, correlation ID when applicable, duration, and outcome.

## Levels

- **DEBUG:** investigation detail, disabled by default in production.
- **INFO:** lifecycle and completed operations.
- **WARNING:** recoverable degradation, fallback, retry, nearing limits, deprecation.
- **ERROR:** failed operation requiring attention.
- **CRITICAL:** immediate system-wide integrity, availability, or safety risk.

Expected user errors should not emit stack traces unless verbose diagnostics are enabled.

## Never log

Passwords, access/refresh tokens, cookies, sessions, private keys, seed phrases, authorization headers, connection strings, raw personal records, vulnerability payloads, or full bodies by default.

Redact before formatting and prefer allowlisted fields. The example regex filter is a backstop, not permission to log arbitrary data.

## Retention and access

Define readers, storage, retention, deletion/legal holds, and encryption. Keep debug logs shorter than security audit logs. Sanitize logs before public issue attachment.
