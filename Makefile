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
migrations:
	@echo "Making migrations..."
	docker compose exec web python3 manage.py makemigrations
	@echo "Applying migrations to the database..."
	docker compose exec web python3 manage.py migrate --noinput
user_migrations:
	@echo "Making migrations for the users app..."
	docker compose exec web python3 manage.py makemigrations users
	@echo "Applying migrations to the database..."
	docker compose exec web python3 manage.py migrate
all_migrations:
	@echo "Making migrations for the users app..."
	docker compose exec web python3 manage.py makemigrations users
	@echo "Applying migrations to the database..."
	docker compose exec web python3 manage.py migrate
	@echo "Making migrations..."
	docker compose exec web python3 manage.py makemigrations
	@echo "Applying migrations to the database..."
	docker compose exec web python3 manage.py migrate --noinput
startapp:
	docker compose exec web python manage.py startapp $(name)
test:
	docker compose exec web pytest -rP
test_app:
	docker compose exec web pytest -rP $(ARGS)
reservation_dummy_data:
	docker compose exec web python manage.py populate_dummy_reservation
order_menuitems_dummy_data:
	docker compose exec web python manage.py populate_dummy_menu_items
menuitems_dummy_data:
	docker compose exec web python manage.py populate_dummy_menuitems
superuser:
	docker compose exec web python manage.py createsuperuser
delete_migrations:
	python remove_migrations.py
nuke: 
	@echo "Removing migration files..."
	python remove_migrations.py
	@echo "Removing all Docker containers..."
	-docker rm -f $(shell docker ps -a -q)
	@echo "Removing all Docker images..."
	-docker rmi -f $(shell docker images -q)
	@echo "Removing all Docker volumes..."
	-docker volume rm $(shell docker volume ls -q)
	@echo "Removing all user-defined Docker networks..."
	-docker network rm $(shell docker network ls -q -f type=custom)
	@echo "Docker cleanup complete."
	docker-compose up --build -d --remove-orphans
	@echo "Docker build complete."
	@echo "Making migrations for the users app..."
	docker compose exec web python3 manage.py makemigrations users
	@echo "Applying migrations to the database..."
	docker compose exec web python3 manage.py migrate
	@echo "Making migrations..."
	docker compose exec web python3 manage.py makemigrations
	@echo "Applying migrations to the database..."
	docker compose exec web python3 manage.py migrate --noinput
	docker compose exec web python manage.py createsuperuser




