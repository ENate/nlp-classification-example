airflow-init:
	docker compose up airflow-init
start:
	docker-compose up -d
stop:
	docker compose down --volumes --remove-orphans
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