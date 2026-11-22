#!/usr/bin/env bash
# Install the wheel outside the source tree using one stable Core release.
set -euo pipefail
wheel="${1:?wheel path required}"
root=$(cd "$(dirname "$0")/.." && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
tag=$(curl -fsSL --retry 3 https://api.github.com/repos/home-assistant/core/releases/latest | jq -er '.tag_name | select(test("^[0-9]{4}\\.[0-9]+\\.[0-9]+$"))')
source_url="https://raw.githubusercontent.com/home-assistant/core/$tag"
python=$(curl -fsSL --retry 3 "$source_url/.python-version")
echo "Testing Home Assistant $tag on Python $python"
curl -fsSL --retry 3 "$source_url/homeassistant/package_constraints.txt" -o "$work/constraints.txt"
"$root/tools/test-distribution.sh" "$wheel" "$python" "$work/constraints.txt"
