"""Defines initial DAG."""
import sys
import os
import pendulum
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from src.models.initial_model_functions import load_preprocess, fit_model

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


PATH_STREAM_SAMPLE = "/data/stream_sample.p"
PATH_TEST_SET = "/data/test_set.p"
INITIAL_MODEL_PATH = "/models/current_model/initial_model.H5"

BATCH_SIZE = 128
NUM_CLASSES = 10
EPOCHS = 4
local_tz = pendulum.timezone("Europe/Amsterdam")
with DAG (
    "initial_model_DAG",
    default_args = {
    'owner': 'airflow',
    # this in combination with catchup=False ensures the
    # DAG being triggered from the
    # current date onwards along the set interval
    'start_date': pendulum.datetime(2024, 10, 24, tz=local_tz),
    # 'start_date': airflow.utils.dates.days_ago(0, 0, 0, 10, 0),
    # this is set to True as we want to pass variables on
    # from one task to another
    'provide_context': True,
    # dag_id='initial_model_DAG',
    # default_args=args,
    # set interval
    },
    description= "Initial DAG",
    schedule = "@once",
    # indicate whether or not Airflow should do any runs for
    # intervals between the start_date and the current date that
    # haven't been run thus far
	catchup=False
) as dag:
    task1 = PythonOperator(
    task_id='load_preprocess',
    python_callable=load_preprocess,        # function to be executed
    op_kwargs={'path_stream_sample': PATH_STREAM_SAMPLE,        # input arguments
			'path_test_set': PATH_TEST_SET},
    # dag=dag,
    )
    task2 = PythonOperator(
    task_id='fit_model',
    python_callable=fit_model,
    op_kwargs={'batch_size': BATCH_SIZE,
            'epochs': EPOCHS,
			'num_classes': NUM_CLASSES,
            'initial_model_path': INITIAL_MODEL_PATH},
    )
    task1 >> task2                  # set task priority
