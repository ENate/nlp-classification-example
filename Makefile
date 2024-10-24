airflow-init:
	docker-compose -f docker/docker-compose.yml up airflow-init
start:
	docker-compose -f docker/docker-compose.yml up --remove-orphans -d
stop:
	docker-compose -f docker-compose.yml down --volumes --remove-orphans
logs-postgres:
	docker compose logs postgres
logs-redis:
	docker compose logs redis
logs-flower:
	docker compose logs flower
logs-worker:
	docker compose logs airflow-worker
logs-scheduler:
	docker compose logs airflow-scheduler