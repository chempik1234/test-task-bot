up:
	docker	compose -f ./docker/docker-compose.yaml up -d

upd:
	docker compose -f ./docker/docker-compose.yaml up -d --build

down:
	docker compose -f ./docker/docker-compose.yaml down

deldb:
	docker volume rm docker_postgres_data

freezeb:
	 pip freeze > .\bot\requirements.txt

updbot:
	docker compose -f ./docker/docker-compose.yaml up -d --build bot1

logsbot:
	docker compose -f ./docker/docker-compose.yaml logs bot1

restart:
	docker compose -f ./docker/docker-compose.yaml restart $(ARGS)
