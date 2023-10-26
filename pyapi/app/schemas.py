from pydantic import BaseModel,EmailStr
from datetime import datetime

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True

class PostCreated(PostBase):
    pass 

class Post(PostBase):
    # title : str
    # content : str
    # published : bool
    class Config:
        orm_mode=True

class UserCreated(BaseModel):
    email : EmailStr
    password : str
    