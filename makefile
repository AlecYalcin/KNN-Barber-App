# Rodando aplicações localmente

run-build:
	docker-compose down
	docker-compose up --build

run:
	docker-compose down
	docker-compose up