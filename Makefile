init:
	pip install pipenv
	pipenv install --dev

flake8:
	pipenv run flake8

test:
	pipenv run pytest tests

coverage:
	pipenv run pytest --cov

