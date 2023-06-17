from pydantic import BaseModel

from .users import User


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    
    
    class Config:
        orm_mode = True

class PostOut(Post):
    owner: User
    
    class Config:
        orm_mode = True
