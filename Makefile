.PHONY: run lint format up shell

run:
	@FLASK_APP=fridge flask run

lint:
	@pylint ./**/*.py

format:
	@autopep8 --in-place --aggressive --aggressive ./**/*.py

up:
	@docker-compose up

shell:
	@pipenv shell