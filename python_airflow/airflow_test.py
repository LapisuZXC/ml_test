from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="demo", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:
    default_args={
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),  # timedelta из пакета datetime
    }
    # Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello")
    run_this = BashOperator(task_id="run_this", bash_command="pwd")
    def print_message(message, ds=None):
        print("kwargs:")
        print(message)
        print("variable ds:")
        print(ds)
    py_op_test = PythonOperator(
            task_id="py_op_test",
            python_callable=print_message,
            op_kwargs={"message": "message"}
            )
    # Set dependencies between tasks
    hello >> py_op_test >> run_this


