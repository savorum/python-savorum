# Development

Use the Python and uv versions in `.tool-versions`. Run the release checks
from the repository root:

```sh
dist_dir=$(mktemp -d)
tools/check.sh "$dist_dir"
tools/test-distribution.sh "$dist_dir"/*.tar.gz 3.11
tools/test-distribution.sh "$dist_dir"/*.whl "$(awk '$1 == "python" {print $2}' .tool-versions)"
```

The SDK checks cover the lockfile, lint, formatting, types, tests, generated
sources, known dependency advisories, and distribution metadata. Coverage is
enforced at 100% for the hand-written package. The distribution checks exercise the source
archive on the minimum supported Python and the wheel on the SDK toolchain.

## Home Assistant compatibility

An independent weekly workflow installs the wheel with the Python version and
dependency constraints from the latest stable Home Assistant Core release.
It runs the SDK suite and reports its own result. To check a candidate wheel
before the first public release, run:

```sh
tools/check-home-assistant.sh "$dist_dir"/*.whl
```

## Generated client

`api/upstream.json` records the Savorum Core commit and SHA-256 digest of
`api/openapi.json`. The generator and its dependencies are locked in `uv.lock`.

```sh
python tools/regenerate.py --fetch
python tools/regenerate.py --check
```

The weekly update resolves the current upstream revision and fetches the schema
from that commit. An unchanged schema needs no update. A changed schema is
regenerated and tested with read-only permissions. A separate job applies the
schema, pin, and generated files to a single update branch and opens or updates
its pull request. Regenerate locally with `python tools/regenerate.py` after
changing the generator or its configuration. Run `tools/drift.sh ../savorum`
to inspect other upstream API changes against a local checkout.

## Installed distribution

Build and install the wheel, then run the smoke test outside the checkout. It
checks that `py.typed`, the generated client, credentials, and response parsing
are present in the installed distribution.

```sh
uv build
python3 -m pip install --force-reinstall dist/aiosavorum-*.whl
cd "$(mktemp -d)"
python3 /path/to/python-savorum/tools/installed.py
```

## Release

Update `CHANGELOG.md` and the version in `pyproject.toml` and
`aiosavorum/__init__.py`, then tag the commit as `vX.Y.Z`. The release workflow
checks lint, types, tests, and regeneration, builds both distributions, checks
their metadata, and publishes them to PyPI with Trusted Publishing. The PyPI
project must grant the `savorum/python-savorum` repository permission to publish
from the `pypi` environment.
