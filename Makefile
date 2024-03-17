ifneq (,$(wildcard ./.env))
	include .env
	export
	ENV_FILE_PARAM = --env-file .env
endif

build:
	docker compose up --build -d --remove-orphans
up:
	docker compose up
down: 
	docker compose down
logs:
	docker compose logs
migrate:
	docker compose exec api python3 manage.py migrate --noinput
makemigrations:
	docker compose exec api python3 manage.py makemigrations