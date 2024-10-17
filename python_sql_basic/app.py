from fastapi import FastAPI, HTTPException, Depends
import datetime
from pydantic import BaseModel
import json
import psycopg2
import dotenv
import os
 # Загрузить переменные окружения

dotenv.load_dotenv()

# Получить переменную окружения
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")





def get_db():
    conn = connection = psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
    return conn


class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: datetime.date


app = FastAPI()

@app.get("/")
async def root(a: int, b: int):
    return {"message":f"{a+b}"}

@app.get("/sum_date")
async def date(current_date: datetime.date, offset: int):
    return current_date + datetime.timedelta(days=offset)

@app.post("/user/validate")
def functi(name: str, surname: str, age: int, registration_date: datetime.date):
    try:
        u = User(name=name, surname=surname, age=age, registration_date=registration_date)
        return {"message":f"Will add user: {u.name} {u.surname} with age {u.age}"}
    except:
        raise HTTPException(status_code=402)

@app.get("/user/{id}")
async def getuser(id: int, db=Depends(get_db)):
    try:
        with db.cursor() as cursor:
            cursor.execute('''
                   SELECT gender, age, city FROM "user"
                WHERE id = %s 
                       ''', (id,))

            user = cursor.fetchone()
    
            return {"gender": user[0], "age": user[1], "city": user[2]}
    except:
        raise HTTPException(status_code=404,detail="user not found")

class PostResponce(BaseModel):
    id: int
    text: str
    topic: str
    class Config:
        orm_mode = True

@app.get("/post/{id}", response_model=PostResponce)
async def getpost(id: int, db=Depends(get_db)):
    try:
        with db.cursor() as cursor:
            cursor.execute('''
                           SELECT * FROM post
                           WHERE id = %s
                           ''', (id,))
            pre_result = cursor.fetchone()
            result = {"id": pre_result[0], "text": pre_result[1], "topic": pre_result[2]}
            return PostResponce(**result)
    except:
        raise HTTPException(status_code=404, detail="post not found")


