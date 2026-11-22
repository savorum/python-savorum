# Contributing to aiosavorum

Follow the [code of conduct](CODE_OF_CONDUCT.md) when participating in the
project. Contributions are distributed under the [MIT license](LICENSE.txt).

## Report a problem

A defect report or regression-test pull request should include the Python,
aiosavorum, and Savorum server versions. Give the SDK call, the expected
result, and the smallest example that shows the difference. For HTTP failures,
include the status and API error code when available. Remove tokens, session
cookies, and private recipe data. Report security problems privately using the
[security policy](SECURITY.md).

## Set up a checkout

From the repository root, install the Python and uv versions in
`.tool-versions` with [mise](https://mise.jdx.dev/), then sync the environment:

```sh
mise install
uv sync --locked --group dev
uv run pytest
```

## Change the client

The handwritten API lives in `aiosavorum/`. Keep public entry points async
and typed. An application that supplies its own HTTP client retains ownership
of its connection pool and default headers.

The wire models and endpoints in `aiosavorum/_generated/` come from the
pinned OpenAPI schema. Follow the [generation instructions](docs/development.md#generated-client)
when changing the pin or generator settings. Review the resulting diff for
changes to public arguments, return types, and errors.

Test changes through the public SDK method. For a write, check the outgoing
headers and payload as well as the returned model. For a streaming change,
exercise an unbuffered response, including interruption or cancellation when
relevant. Use small synthetic fixtures that can ship with the repository.

## Submit a change

1. Keep the pull request focused. Explain the observable behavior and how you tested it.
2. Update the [usage guide](docs/usage.md) and [changelog](CHANGELOG.md) when a public contract changes.
3. Run the [release checks](docs/development.md) against the checkout and built wheel.
4. Sign off each commit with `git commit -s`. The sign-off certifies the
   [Developer Certificate of Origin](https://developercertificate.org/) and
   must match the commit author's name and email address. CI exempts merge commits
   and commits authored by `dependabot[bot]`.
