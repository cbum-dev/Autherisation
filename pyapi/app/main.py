from fastapi import FastAPI,status,Response,HTTPException,Depends
from typing import Optional
from fastapi.params import Body #to display output in body of terminal .
from pydantic import BaseModel
from random import randrange
import psycopg2
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine,get_db

models.Base.metadata.create_all(bind = engine)

app = FastAPI()



my_post = [{"title":"Dhoom","content":"nothing","id":1},
           {"title":"Dhoom2","content":"nothing2","id":2}
           ]

def find_index(id):
    for i , p in enumerate(my_post):
        if p['id'] == id:
            return i 

class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating : Optional[int] = None

while True:
    try:
        conn = psycopg2.connect(host = "localhost",database = "db_test",user = "postgres" , password = "",cursor_factory=RealDictCursor)
        cursor  = conn.cursor()
        print("DB CONNECTED")
        break
    except Exception as error:
        print("hi",error)



@app.get("/")
def read_root():
    cursor.execute(""" SELECT * FROM post ORDER BY title""")
    posts = cursor.fetchall()
    return {"data":posts}
    # return {"Hello": my_post}

@app.post("/post",status_code=status.HTTP_201_CREATED) 
# def create(payLoad: dict = Body(...)): # created a ducntion with variable payload and with dictory bin the body.
#     print(payLoad)
#     return {"message" : f"title{payLoad['todo_name']} content{'todo_description'}"}
# def create_post(post : Post):
#     # print(post)                     
#     # print(post.dict())
#     post_dict = post.dict()
#     post_dict['id'] = randrange(0,1999999)
#     my_post.append(post_dict)
def create_post(post : Post):
    cursor.execute(""" INSERT INTO post(title,content,published) VALUES
                   (%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data" : "created SUCCESSFULLY: ","post" : new_post}
    
    # return {"data" : post_dict}

# @app.get("/post/{id}")
# def get_post(id : int , response : Response):
#     post = find_post
@app.delete("/post/{id}" , status_code=status.HTTP_204_NO_CONTENT )
def delete_post(id : int):
    cursor.execute("""DELETE FROM post where id = %s RETURNING *""", (str(id),))
    deleted = cursor.fetchone()
    conn.commit()
    if deleted == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with this {id} doesn't exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/post/{id}")
def update_post(id : int, post : Post):
    cursor.execute("""UPDATE post SET title = %s, content = %s, published = %s WHERE id = %s 
                   RETURNING *""" ,(post.title,post.content,post.published,str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with this {id} doesn't exist")

    return {"data": updated_post}

@app.get("/sql")
def test_post(db : Session = Depends(get_db)):
    posts = db.query(models.Posts).all()
    return {"data" : posts}