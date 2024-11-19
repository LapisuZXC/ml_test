from airflow.hooks.base import BaseHook

import psycopg2
import os
import dotenv

os.chdir(os.getcwd())

dotenv.load_dotenv("../.")

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")


def get_db():
    conn = connection = psycopg2.connect(
        database=db_name, user=db_user, password=db_password, host=db_host, port=db_port
    )
    return conn
