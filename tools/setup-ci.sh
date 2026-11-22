#!/usr/bin/env bash
set -euo pipefail

tool_env="$RUNNER_TEMP/ci-tools"
python3 -m venv "$tool_env"
uv_version=$(awk '$1 == "uv" {print $2}' .tool-versions)
# Digest of the Linux x86_64 wheel distributed on PyPI.
echo "uv==$uv_version --hash=sha256:d7f459fe4fd247d830351c75686d3996ace3c6f3f728eb0e85a30b7ada0cef19" |
    "$tool_env/bin/pip" install --only-binary=:all: --no-deps --require-hashes -r /dev/stdin
echo "$tool_env/bin" >> "$GITHUB_PATH"
awk '$1 == "python" {print "UV_PYTHON=" $2}' .tool-versions >> "$GITHUB_ENV"
