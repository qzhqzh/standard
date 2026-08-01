.PHONY: install format lint typecheck test self-check build check clean

install:
	python -m pip install -e '.[dev]'

format:
	ruff format .
	ruff check --fix .

lint:
	ruff format --check .
	ruff check .

typecheck:
	mypy src

test:
	python -m unittest discover -s tests -v

self-check:
	python -m repo_standard check . --policy standard.toml --fail-level recommended

build:
	python -m build

check: lint typecheck test self-check build

clean:
	rm -rf build dist .mypy_cache .ruff_cache src/*.egg-info src/repo_standard.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
