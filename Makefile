.PHONY: run lint format up shell create_migration up_migration down_migration psql repl

run:
	@FLASK_APP=autoapp FLASK_DEBUG=1 flask run

create_migration:
	@FLASK_APP=autoapp flask db migrate

up_migration:
	@FLASK_APP=autoapp flask db upgrade

down_migration:
	@FLASK_APP=autoapp flask db downgrade

lint:
	@pylint ./**/*.py

format:
	@autopep8 --in-place --aggressive ./**/*.py

up:
	@docker-compose up

shell:
	@pipenv shell

psql:
	@psql -U postgres -h 127.0.0.1 -p 5432

repl:
	FLASK_APP=autoapp flask shell