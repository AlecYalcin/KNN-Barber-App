# Rodando aplicações localmente

run-docker:
	docker-compose down && docker-compose up &

run-backend:
	cd back && uvicorn src.entrypoints.fastapi:app --reload &

run-frontend:
	echo "NotImplemented" &

run:
	make run-docker
	make run-backend
	make run-frontend