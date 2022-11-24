.ONESHELL:
SHELL:= /bin/bash
.SHELLFLAGS += -e


DJANGO_ROOT=project13

echo-django:
	source .env_development
	echo ${DJANGO_ROOT}

# Env setup
env-install:
	source .env_development
	pip install -r project13/requirements.txt

# Django commands
django-makemigrations:
	source .env_development && cd ${DJANGO_ROOT}
	python manage.py makemigrations

django-migrate:
	source .env_development && cd ${DJANGO_ROOT}
	python manage.py migrate

django-test:
	source .env_testing && cd ${DJANGO_ROOT}
	python manage.py collectstatic --noinput
	python manage.py test

django-linter:
	source .env_development && cd ${DJANGO_ROOT}
	flake8 --exclude=env

django-start:
	source .env_development && cd ${DJANGO_ROOT}
	python manage.py collectstatic --noinput
	python manage.py runserver

django-static:
	source .env_development && cd ${DJANGO_ROOT}
	python manage.py collectstatic --noinput

docker-build:
	docker build -t  local/oc-lettings .
