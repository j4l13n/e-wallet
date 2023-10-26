.PHONY: all help translate test clean update compass collect rebuild

# target all - Default target. Does nothing.
all:
		@echo "Hello ${LOGNAME}, nothing to do by default"
		@echo "Try 'make help'"

build:
		docker-compose build

run-dev:
		docker-compose down && docker-compose up

run-migrate:
		docker-compose run app sh -c "python manage.py migrate"

shell:
		docker-compose run app sh

rebuild:
		docker-compose down && docker-compose up --build --force-recreate

clean:
		docker-compose down

test:
		docker-compose run app sh -c "pytest"

help:
		@echo "Hello ${LOGNAME}, nothing to do by default"

		@echo "*Build container*"
		@echo "> make build"
		@echo "*Run development*"
		@echo "> make run-dev"
		@echo "*Run migration*"
		@echo "> make run-migrate"

logs:
		docker-compose logs -f app
