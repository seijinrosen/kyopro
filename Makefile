init:
	python3.8 -m venv .venv/
	poetry install
	direnv allow
	pnpm install
