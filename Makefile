dummy:
	echo dummy

open:
	gh repo view --web

prepare-atcoder:
	cargo run --bin prepare_atcoder

update:
	python -m pip install --upgrade pip setuptools
	poetry update
	pnpm update

git-reset:
	git reset --soft HEAD^

init:
	python3.8 -m venv .venv/
	poetry install
	direnv allow
	pnpm install
