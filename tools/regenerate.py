#!/usr/bin/env python3
"""Regenerate the isolated OpenAPI client from the pinned contract."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "api" / "openapi.json"
CONFIG_PATH = ROOT / "generator-config.yaml"
GENERATED_PATH = ROOT / "aiosavorum" / "_generated"

PIN_PATH = ROOT / "api" / "upstream.json"
UPSTREAM_REPOSITORY = "https://github.com/savorum/savorum.git"


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _upstream_commit() -> str:
    git = shutil.which("git")
    if git is None:
        message = "git is required to resolve the upstream commit"
        raise SystemExit(message)
    result = subprocess.run(  # noqa: S603
        [git, "ls-remote", "--exit-code", UPSTREAM_REPOSITORY, "refs/heads/main"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    commit = result.stdout.split()[0]
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        msg = "invalid upstream commit"
        raise ValueError(msg)
    return commit


def _fetch_upstream() -> tuple[str, bytes]:
    """Resolve main once and download the schema at that exact revision."""
    commit = _upstream_commit()
    url = f"https://raw.githubusercontent.com/savorum/savorum/{commit}/api/openapi.json"
    with urlopen(url, timeout=30) as response:
        data = response.read()
    return commit, data


def _verify_spec() -> bytes:
    expected = json.loads(PIN_PATH.read_text())["sha256"]
    data = SPEC_PATH.read_bytes()
    digest = _sha256(data)
    if digest != expected:
        msg = f"api/openapi.json digest is {digest}, expected {expected}"
        raise SystemExit(msg)
    return data


def _run_generator(spec: Path, destination: Path) -> None:
    command = [
        "uv",
        "run",
        "--locked",
        "--group",
        "dev",
        "openapi-python-client",
        "generate",
        "--path",
        str(spec),
        "--config",
        str(CONFIG_PATH),
        "--meta=none",
        "--output-path",
        str(destination),
    ]
    subprocess.run(command, cwd=ROOT, check=True)  # noqa: S603


def _snapshot(root: Path) -> dict[str, bytes]:
    return {
        str(path.relative_to(root)): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }


def _compare(generated: Path, target: Path) -> int:
    expected = _snapshot(generated)
    actual = _snapshot(target) if target.exists() else {}
    if expected == actual:
        print(f"generated client matches {GENERATED_PATH.relative_to(ROOT)}")
        return 0

    for name in sorted(expected.keys() | actual.keys()):
        if expected.get(name) != actual.get(name):
            print(f"diff: {name}")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="compare generated output with the checked-in client",
    )
    parser.add_argument(
        "--fetch",
        action="store_true",
        help="download upstream main and move the pin when the contract changed",
    )
    args = parser.parse_args()

    before = _verify_spec()
    with tempfile.TemporaryDirectory(prefix="aiosavorum-generate-") as temp_dir:
        spec = SPEC_PATH
        pin = None
        if args.fetch:
            commit, data = _fetch_upstream()
            if data != before:
                spec = Path(temp_dir) / "openapi.json"
                spec.write_bytes(data)
                pin = {"commit": commit, "sha256": _sha256(data)}
            elif not args.check:
                print("upstream OpenAPI contract is unchanged")
                return 0

        generated = Path(temp_dir) / "client"
        _run_generator(spec, generated)
        if _verify_spec() != before:
            message = "OpenAPI document changed during generation"
            raise SystemExit(message)
        if args.check:
            return _compare(generated, GENERATED_PATH) or int(pin is not None)

        shutil.rmtree(GENERATED_PATH, ignore_errors=True)
        shutil.copytree(generated, GENERATED_PATH)
        if pin is not None:
            SPEC_PATH.write_bytes(spec.read_bytes())
            PIN_PATH.write_text(json.dumps(pin, indent=2) + "\n")
        print(f"wrote {GENERATED_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
