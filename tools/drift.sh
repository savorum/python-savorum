#!/usr/bin/env bash
# Report how far the pinned Savorum Core revision is behind upstream.
set -euo pipefail

root="${1:-../savorum}"
pin="$(dirname "$0")/../api/upstream.json"
declared="${SAVORUM_COMMIT:-$(jq -er .commit "$pin")}"

upstream="$(git -C "$root" rev-parse origin/main)"
echo "declared: $declared"
echo "upstream: $upstream (origin/main)"

if [ "$declared" = "$upstream" ]; then
    echo "the pin is current"
    exit 0
fi

if ! git -C "$root" cat-file -e "${declared}^{commit}" 2>/dev/null; then
    echo "the declared revision is not in this checkout, so nothing can be compared" >&2
    exit 2
fi

echo "upstream is $(git -C "$root" rev-list --count "$declared..$upstream") commit(s) ahead:"
git -C "$root" log --oneline "$declared..$upstream" | sed 's/^/  /'

echo
echo "changes in the contract and the behaviour this client is tested against:"
changed="$(git -C "$root" diff --name-only "$declared..$upstream" -- api internal/api/v1 docs/reference/security-threat-model.md docs/reference/resource-lifecycle.md)"
if [ -n "$changed" ]; then
    printf '%s\n' "$changed"
    echo
    echo "review these before moving the pin"
else
    echo "  none"
fi
exit 1
