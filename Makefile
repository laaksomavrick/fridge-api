.PHONY: run lint

run:
	@FLASK_APP=fridge/main.py flask run

lint:
	@pipenv run pylint ./**/*.py

format:
	@pipenv run autopep8 --in-place --aggressive --aggressive ./**/*.py