help:
	@echo "make test"

test:
	-docker-compose run django_app pytest --show-capture=no --disable-pytest-warnings

test-p:
	-docker-compose run django_app pytest --show-capture=no --disable-pytest-warnings ${p}

local:
	-docker-compose up

build:
	-docker-compose up --build

push:
	-git push origin dev

down:
	-docker-compose down

migration:
	-docker-compose run django_app python manage.py makemigrations

migrate:
	-docker-compose run django_app python manage.py migrate

new:
	-docker-compose run django_app python manage.py startapp ${app}

seeds:
	-docker-compose run django_app python manage.py seeds ${i}

bash:
	-docker-compose run django_app bash

superuser:
	-docker-compose run django_app python manage.py createsuperuser

black:
	-docker-compose run django_app black -S .


coverage:
	-docker-compose run django_app pytest --cov
	-docker-compose run django_app coverage html

shell:
	-docker-compose run django_app python manage.py shell