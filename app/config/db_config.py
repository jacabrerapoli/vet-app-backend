import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

ENGINE_DB = "mysql+pymysql"
USER_DB = os.environ["USER_DB"]
PASSWORD_DB = os.environ["PASSWORD_DB"]
HOST_DB = os.environ["HOST_DB"]
PORT = os.environ["PORT_DB"]
DATABASE_DB = os.environ["DATABASE_NAME_DB"]

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
