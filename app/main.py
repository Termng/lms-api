from fastapi import FastAPI, Response, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .routers import course, enrollment, lesson, question, submission, user
from .database import engine, get_db
from sqlalchemy.orm import Session
from . import models, schema,database
app = FastAPI()



models.Base.metadata.create_all(bind=engine)

# app.include_router(course.router)
# app.include_router(enrollment.router)
# app.include_router(lesson.router)
# app.include_router(question.router)
# app.include_router(submission.router)
app.include_router(user.router)



while True:   
    try:
        conn = psycopg2.connect(host='localhost', database = 'LMS' , user = 'postgres', password = 'Merciful', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Connection to Postgres was successful')
        break
    except Exception as error:
        print('connection failed')
        print("Error: ", error)
        time.sleep(4)



@app.get("/")
def root():
    return {"message": "Hello World"}