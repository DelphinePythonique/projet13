.ONESHELL:
SHELL:= /bin/bash
.SHELLFLAGS += -e


# Environment variables
DEVELOPMENT_SETTINGS=project.settings
TEST_SETTINGS=project.test_settings
DJANGO_ROOT=project13

echo-django:
	echo ${DJANGO_ROOT}

# Env setup
env-install:
	source .env
	pip install -r requirements.txt

# Django commands
django-makemigrations:
	source .env && cd ${DJANGO_ROOT}
	python manage.py makemigrations --settings=${DEVELOPMENT_SETTINGS}

django-migrate:
	source .env && cd ${DJANGO_ROOT}
	python manage.py migrate --settings=${DEVELOPMENT_SETTINGS}

django-test:
	source .env && cd ${DJANGO_ROOT}
	python manage.py collectstatic --noinput --settings=${TEST_SETTINGS}
	python manage.py test --settings=${TEST_SETTINGS}

django-start:
	source .env && cd ${DJANGO_ROOT}
	python manage.py collectstatic --noinput --settings=${DEVELOPMENT_SETTINGS}
	python manage.py runserver --settings=${DEVELOPMENT_SETTINGS}