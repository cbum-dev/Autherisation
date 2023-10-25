from fastapi import FastAPI,status,Response,HTTPException
from typing import Optional
from fastapi.params import Body #to display output in body of terminal .
from pydantic import BaseModel
from random import randrange


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



@app.get("/")
def read_root():
    return {"Hello": my_post}

@app.post("/post",status_code=status.HTTP_201_CREATED) 
# def create(payLoad: dict = Body(...)): # created a ducntion with variable payload and with dictory bin the body.
#     print(payLoad)
#     return {"message" : f"title{payLoad['todo_name']} content{'todo_description'}"}
def create_post(post : Post):
    # print(post)                     
    # print(post.dict())
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1999999)
    my_post.append(post_dict)
    
    return {"data" : post_dict}

# @app.get("/post/{id}")
# def get_post(id : int , response : Response):
#     post = find_post
@app.delete("/post/{id}" , status_code=status.HTTP_204_NO_CONTENT )
def delete_post(id : int):
    index = find_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with this {id} doesn't exist")
    my_post.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/post/{id}")
def update_post(id : int, post : Post):
    index = find_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with this {id} doesn't exist")
    post_dict = post.dict()
    post_dict['id'] = id
    my_post[index] = post_dict
    return {"data": post_dict}