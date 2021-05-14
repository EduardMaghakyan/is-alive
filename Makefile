tdd:
	poetry run ptw src

test:
	poetry run mypy src/
	poetry run flake8 --exclude alembic src/
	poetry run isort --gitignore --check-only src/
	poetry run black --check --diff src/
	poetry run safety check
	poetry run bandit -x tests,static_ -r src/
	poetry run pytest src/

coding_standard:
	poetry run isort --gitignore src/
	poetry run black src/

build:
	docker build -f Dockerfile -t is-alive . --rm
