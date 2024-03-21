ifneq (,$(wildcard ./.env))
	include .env
	export
	ENV_FILE_PARAM = --env-file .env
endif

.PHONY: build up down logs migrate makemigrations testcoverage startapp

build:
	docker compose up --build -d --remove-orphans
up:
	docker compose up -d
down: 
	docker compose down
logs:
	docker compose logs
testcoverage: 
	docker compose exec web coverage run manage.py test 
migrate:
	docker compose exec web python3 manage.py migrate --noinput
makemigrations:
	docker compose exec web python3 manage.py makemigrations
startapp:
	docker compose exec web python manage.py startapp $(name)
test:
	docker compose exec web pytest -rP