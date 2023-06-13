from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#DB_URL = "postgresql://<username>:<password>@<ip>/migrations"
DB_URL = "postgresql://postgres:postgres@127.0.0.1:5432/migrations"

engine = create_engine(url=DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()