setup:
	curl -sSL https://install.python-poetry.org | python3 - --version 1.4.2
	poetry config virtualenvs.in-project true
	poetry update
	poetry lock
	poetry install
	poetry run pre-commit install
