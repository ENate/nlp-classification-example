"""Streams of data injestion from kafka topics"""
import pendulum
from airflow.models import DAG
from airflow.providers.apache.kafka.operators.produce import ProduceToTopicOperator
from src.data.kafka_producer import generate_stream


PATH_STREAM_SAMPLE = "/data/stream_sample.p"
local_tz = pendulum.timezone("Europe/Amsterdam")
with DAG (
    "stream_DAG",
    default_args = {
        'owner': 'airflow',
        # this in combination with catchup=False ensures the DAG being
        # triggered from the current date onwards along the set interval
        #'start_date': airflow.utils.dates.days_ago(1),
        'start_date': pendulum.datetime(2024, 10, 24, tz=local_tz),
        # this is set to True as we want to pass variables on from one task to another
        'provide_context': True,
    },
    schedule = "@hourly",      # set interval
    # indicate whether or not Airflow should do any runs for intervals between
    # the start_date and the current date that haven't been run thus far
    catchup=False,
) as dag:
    task1 = ProduceToTopicOperator(
    task_id='generate_stream',
    topic='Topic A',
    producer_function=generate_stream,
    producer_function_kwargs={'path_stream_sample': PATH_STREAM_SAMPLE}
)
