from fastapi import FastAPI,status,Response,HTTPException,Depends
from typing import Optional,List
from fastapi.params import Body #to display output in body of terminal .
from pydantic import BaseModel
from random import randrange
import psycopg2
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor
from . import models,utils
from . import schemas
from .database import engine,get_db

from .routers import post,users

models.Base.metadata.create_all(bind = engine)

app = FastAPI()


class Post(BaseModel):
    title : str
    content : str
    published : bool = True

while True:
    try:
        conn = psycopg2.connect(host = "localhost",database = "db_test",user = "postgres" , password = "",cursor_factory=RealDictCursor)
        cursor  = conn.cursor()
        print("DB CONNECTED")
        break
    except Exception as error:
        print("hi",error)

app.include_router(post.router)
app.include_router(users.router)