airflow-init:
	sh echo -e "AIRFLOW_UID=$(id -u)" > .env
	docker compose up airflow-init
	docker compose down --volumes --remove-orphans 
start:
	docker compose up --remove-orphans -d
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