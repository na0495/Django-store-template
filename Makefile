help:
	@echo "make test"

test:
	-docker-compose run web_engine_local pytest --show-capture=no --disable-pytest-warnings

test-p:
	-docker-compose run web_engine_local pytest --show-capture=no --disable-pytest-warnings ${p}

local:
	-docker-compose up

build:
	-docker-compose up --build

push:
	-git push origin dev

down:
	-docker-compose down

migration:
	-docker-compose run web_engine_local python manage.py makemigrations

migrate:
	-docker-compose run web_engine_local python manage.py migrate

new:
	-docker-compose run web_engine_local python manage.py startapp ${app}

seeds:
	-docker-compose run web_engine_local python manage.py seeds ${i}

bash:
	-docker-compose run web_engine_local bash

superuser:
	-docker-compose run web_engine_local python manage.py createsuperuser

black:
	-docker-compose run web_engine_local black -S .


coverage:
	-docker-compose run web_engine_local pytest --cov
	-docker-compose run web_engine_local coverage html

shell:
	-docker-compose run web_engine_local python manage.py shell