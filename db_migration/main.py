from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from geoalchemy2 import Geometry

from .db.sql import engine, get_db
from .models import posts


app = FastAPI()

posts.Base.metadata.create_all(bind=engine)


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    
    
    class Config:
        orm_mode = True

class User(BaseModel):
    email: str
    first_name: str
    last_name: str
    
    class Config:
        orm_mode = True


class PostOut(Post):
    owner: User
    
    class Config:
        orm_mode = True
        

class WeatherSource(BaseModel):
    location:Geometry
    location_name: str
    source_type =str
    source_name = str
    
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
        
@app.get("/")
def root():
    return {"message": "success"}


@app.post("/add", response_model=PostOut)
def add_post(post: posts.Post, db: Session = Depends(get_db)):
    new_post = posts.Post(**post.dict(), owner_id=1)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.get("/all")
def get_all_posts(db: Session = Depends(get_db)):
    return db.query(posts.Post).all()

@app.get("/posts/{id}")
def get_post_by_id(id: int, db: Session = Depends(get_db)):
    db.query(posts.Post).filter(posts.Post.id == id).join()
    return db.query(posts.Post).filter(posts.Post.id == id).first()
