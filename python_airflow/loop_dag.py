from datetime import datetime, timedelta
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

with DAG(dag_id="loops", start_date=datetime(2024, 1, 1), schedule="@once") as dag:
    default_args = {
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),  # timedelta из пакета datetime
    }

    def message_exec(task_number: int, **kwargs):
        run_id = kwargs["run_id"]
        ts = kwargs["ts"]
        print(
            f"The task number is {task_number} ;run_id {
                run_id} ; ts {ts}"
        )

    for i in range(30):
        if i < 10:
            bash_op = BashOperator(
                task_id=f"bash_task_at_{i}",
                bash_command="echo $NUMBER",
                env={"NUMBER": str(i)},
            )
            bash_op.doc_md = dedent(
                """\
                ####Task Documentation
                Bash Operator that prints number of current task:
                `bash_command=f"echo $NUMBER"`
        """
            )
        else:
            py_op = PythonOperator(
                task_id=f"python_task_at_{i}",
                python_callable=message_exec,
                op_kwargs={"task_number": i},
                provide_context=True,
            )

            py_op.doc_md = dedent(
                """\
                    ####Task Documentation
                    Python operator that executes function, which prints task number:
                    ```
           def message_exec(task_number: int, **kwargs):
            run_id = kwargs["run_id"]
            ts = kwargs["ts"]
            print(
                f"The task number is {task_number} ;run_id {
                run_id} ; ts {ts}"
                )
                    ```

            """
            )

    [bash_op, py_op]
