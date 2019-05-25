.PHONY: run lint

run:
	@FLASK_APP=src/main.py flask run

lint:
	@pipenv run pylint ./**/*.py

format:
	@pipenv run autopep8 --in-place --aggressive --aggressive ./**/*.py