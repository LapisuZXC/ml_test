from airflow import DAG
from airflow.models.taskinstance import TaskInstance
from airflow.models.dagrun import DagRun
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta


with DAG(dag_id="templates", start_date=datetime(2024,1,1), schedule='@once') as dag:
    default_args={
            'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),  # timedelta из пакета datetime
    }


    for i in range(5):
        tp = BashOperator(task_id=f"bash_operator_{i}", bash_command='echo "ts:{{ ts }}, run_id:{{ run_id }}"')

    tp    
