.PHONY: dev start test lint format install

dev:
	uv run uvicorn src.main:app --reload --host 0.0.0.0 --port 8080

start:
	uv run python -m src.main

test:
	uv run pytest

lint:
	uv run ruff check .

format:
	uv run ruff format .

install:
	uv sync
