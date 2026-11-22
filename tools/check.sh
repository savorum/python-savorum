#!/usr/bin/env bash
set -euo pipefail
export UV_LOCKED=1
uv sync --locked --group dev
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run pytest --cov --cov-report=term-missing
uv run tools/regenerate.py --check
uv audit --locked
uv build --out-dir "${1:?distribution directory required}"
uv run twine check "$1"/*
