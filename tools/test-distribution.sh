#!/usr/bin/env bash
set -euo pipefail
archive="${1:?distribution path required}"
python="${2:?Python version required}"
constraints=()
if [[ -n "${3:-}" ]]; then
    constraints=(--constraint "$3")
fi
root=$(cd "$(dirname "$0")/.." && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
uv venv --python "$python" "$work/env"
uv pip install --python "$work/env/bin/python" ${constraints[@]+"${constraints[@]}"} "$archive" pytest pytest-asyncio hypothesis
cp -R "$root/tests" "$work/tests"
cd "$work"
env/bin/python "$root/tools/installed.py"
env/bin/python -m pytest tests --asyncio-mode=auto -o asyncio_default_fixture_loop_scope=function
