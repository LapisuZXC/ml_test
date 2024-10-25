# Импорт необходимых библиотек и загрузка переменных окружения
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

# Генерация постов для существующих пользователей
post_ids = []  # Список для сохранения идентификаторов постов
for user_id in range(1, 101):  # предполагаем, что у нас 100 пользователей с user_id от 1 до 100
    num_posts = random.randint(0, 10)  # Случайное количество постов от 0 до 10 для каждого пользователя
    for _ in range(num_posts):
        cursor.execute(
            """
            INSERT INTO "post" (text, topic)
            VALUES (%s, %s)
            RETURNING id
            """,
            (
                fake.text(),
                fake.word()
            )
        )
        post_id = cursor.fetchone()[0]  # Получаем id только что созданного поста
        post_ids.append((post_id, user_id))  # Сохраняем связь post_id и user_id

# Коммитим после вставки всех постов
connection.commit()

# Генерация действий пользователей
for post_id, user_id in post_ids:
    viewers = random.sample(range(1, 101), k=random.randint(10, 20))  # Случайные пользователи, которые видят пост
    for viewer_id in viewers:
        # Добавляем просмотр (view) действия
        cursor.execute(
            """
            INSERT INTO "feed_action" (user_id, post_id, action, time)
            VALUES (%s, %s, %s, %s)
            """,
            (
                viewer_id,
                post_id,
                'view',
                fake.date_time_this_year()
            )
        )
        # Добавляем лайк (like) с вероятностью 50%
        if random.choice([True, False]):
            cursor.execute(
                """
                INSERT INTO "feed_action" (user_id, post_id, action, time)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    viewer_id,
                    post_id,
                    'like',
                    fake.date_time_this_year()
                )
            )

# Коммитим после вставки всех действий
connection.commit()

# Закрытие соединения
cursor.close()
connection.close()

