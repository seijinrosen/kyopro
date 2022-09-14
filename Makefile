update:
	python -m pip install --upgrade pip setuptools
	poetry update
	pnpm update

init:
	python3.8 -m venv .venv/
	poetry install
	direnv allow
	pnpm install
