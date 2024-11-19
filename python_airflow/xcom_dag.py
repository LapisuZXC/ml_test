from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import TaskInstance
from datetime import datetime, timedelta


push_task_id = "push_xcom"


def push_data_in_xcom(ti: TaskInstance):
    return "Airflow track everything"


def pull_data_from_xcom(ti: TaskInstance):
    value = ti.xcom_pull(key=push_task_id)
    print(value)


with DAG(dag_id="xcom", start_date=datetime(2024, 1, 1), schedule="@once") as dag:
    default_args = {
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),  # timedelta из пакета datetime
    }
    push_xcom = PythonOperator(
        task_id=push_task_id,
        python_callable=push_data_in_xcom,
    )

    pull_xcom = PythonOperator(
        task_id="pull_xcom",
        python_callable=pull_data_from_xcom,
        provide_context=True
    )

    push_xcom >> pull_xcom
