.PHONY: run install test audit lint typecheck

run:
	npm run dev
install:
	npm i
	uv sync
test:
	cd api && uv run python scripts/create_mock_db.py data/mock_test.db
	cd api && DATABASE_URL=sqlite:///data/mock_test.db uv run pytest tests/ -v
audit: lint typecheck

lint:
	cd api && uv run ruff check . --fix
	cd api && uv run ruff format .

typecheck:
	cd api && uv run pyright .
