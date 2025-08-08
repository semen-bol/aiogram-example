dev-build:
	docker-compose -f deploy/compose.yaml build --no-cache

dev-start:
	docker-compose -f deploy/compose.yaml up --force-recreate --remove-orphans