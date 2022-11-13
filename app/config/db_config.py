import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import  load_dotenv

load_dotenv()

ENGINE_DB = os.getenv("ENGINE_DB")
USER_DB = os.getenv("USER_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")
HOST_DB = os.getenv("HOST_DB")
PORT = os.getenv("PORT_DB")
DATABASE_DB = os.getenv("DATABASE_NAME_DB")

SQLALCHEMY_DATABASE_URL = f"{ENGINE_DB}://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT}/{DATABASE_DB}"

print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
