# Security policy

## Supported versions

The default branch is supported. Other versions do not receive security
maintenance.

## Scope

This library sends credentials to a Savorum instance and decodes untrusted HTTP
responses and server-sent events. A report is in scope when crafted input or an
API response causes any of the following:

- a token, cookie, or `X-Savorum-Library` value to be sent to a different origin
  than the configured base URL;
- an injected client to be closed or have its default headers modified;
- an API error status to be returned as a successful result;
- unbounded memory use, an uncaught exception other than the documented errors,
  or an event stream that cannot be cancelled; or
- a request that bypasses the configured credentials or library scope.

The client sends tokens only in `Authorization` headers. Keep the instance URL
trusted, keep personal tokens out of logs, and use scoped tokens for library
access.

## Reporting

Report a vulnerability privately through GitHub's security advisory form for
this repository. Include the affected version, the request or response shape,
and the impact. Reports are acknowledged within seven days. Do not open a
public issue before the report is resolved.

After confirming a vulnerability, the maintainer coordinates a fix with the
reporter and publishes an advisory identifying affected and fixed versions.
