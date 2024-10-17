import os
from dotenv import load_dotenv
from faker import Faker
import random
import psycopg2

# Загрузить переменные окружения
load_dotenv()

# Получить переменную окружения
db_password = os.getenv("DB_PASSWORD")
# Соединение с базой данных
connection = psycopg2.connect(
    database="db-for-task-6", user="postgres", password=db_password, host="localhost", port="5430"
)
cursor = connection.cursor()

fake = Faker()
# Генерация пользователей
for _ in range(100):
    cursor.execute(
        """
        INSERT INTO "user" (gender, age, country, city, exp_group, os, source)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            random.choice(['Male', 'Female']),
            random.randint(18, 60),
            fake.country()[:50],
            fake.city()[:50],
            random.randint(0, 3),
            random.choice(['iOS', 'Android', 'Windows']),
            fake.domain_name()[:50]
        )
    )

# Коммитим после вставки всех пользователей
connection.commit()

# Генерация постов
for _ in range(50):
    cursor.execute(
        """
        INSERT INTO "post" (text, topic)
        VALUES (%s, %s)
        """,
        (fake.text(), fake.word())
    )

# Коммитим после вставки всех постов
connection.commit()

# Генерация действий пользователей
for _ in range(200):
    cursor.execute(
        """
        INSERT INTO "feed_action" (user_id, post_id, action, time)
        VALUES (%s, %s, %s, %s)
        """,
        (
            random.randint(1, 100),  # Ограничение диапазона до существующих пользователей
            random.randint(1, 50),   # Ограничение диапазона до существующих постов
            random.choice(['like', 'view']),
            fake.date_time_this_year()
        )
    )

# Коммитим после вставки действий
connection.commit()

# Закрытие соединения
cursor.close()
connection.close()

