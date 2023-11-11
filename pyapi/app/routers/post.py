from fastapi import FastAPI,status,Response,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from .. import models,utils
from .. import schemas,oauth2
from ..database import get_db
from typing import Optional,List



router = APIRouter(prefix="/sql",tags=["posts"])
@router.get("/",response_model=List[schemas.Post])
def test_post(db : Session = Depends(get_db)):
    posts = db.query(models.Posts).all()
    return posts

@router.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post : schemas.PostCreated,db:Session = Depends(get_db),):
    # new_post = models.Posts(title = post.title, content = post.content,published = post.published)
    # print(user_id)
    new_post = models.Posts(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int,db:Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with this {id} doesn't exist")    
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code= status.HTTP_204_NO_CONTENT)



 



# #____________________________________________________________________________________
# #Below code is for post table and is written is sql query format.
# @app.get("/")
# def read_root():
#     cursor.execute(""" SELECT * FROM post ORDER BY title""")
#     posts = cursor.fetchall()
#     return posts

# @app.post("/post",status_code=status.HTTP_201_CREATED) 
# # def create(payLoad: dict = Body(...)): # created a ducntion with variable payload and with dictory bin the body.
# #     print(payLoad)
# #     return {"message" : f"title{payLoad['todo_name']} content{'todo_description'}"}
# # def create_post(post : Post):
# #     # print(post)                     
# #     # print(post.dict())
# #     post_dict = post.dict()
# #     post_dict['id'] = randrange(0,1999999)
# #     my_post.append(post_dict)
# def create_post(post : Post):
#     cursor.execute(""" INSERT INTO post(title,content,published) VALUES
#                    (%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
#     new_post = cursor.fetchone()
#     conn.commit()
#     return {"data" : "created SUCCESSFULLY: ","post" : new_post}

# @app.delete("/post/{id}" , status_code=status.HTTP_204_NO_CONTENT )
# def delete_post(id : int):
#     cursor.execute("""DELETE FROM post where id = %s RETURNING *""", (str(id),))
#     deleted = cursor.fetchone()
#     conn.commit()
#     if deleted == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Post with this {id} doesn't exist")
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/post/{id}")
# def update_post(id : int, post : Post):
#     cursor.execute("""UPDATE post SET title = %s, content = %s, published = %s WHERE id = %s 
#                    RETURNING *""" ,(post.title,post.content,post.published,str(id)))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     if updated_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Post with this {id} doesn't exist")

#     return {"data": updated_post}
