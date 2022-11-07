from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
ENGINE_DB = "postgresql+psycopg2"
USER_DB = "root"
PASSWORD_DB = "EOfHM7Dgg6zZ46E5VOKZNiMpi4wgxvNs"
HOST_DB = "dpg-cdiiil4gqg4aiit28o10-a.oregon-postgres.render.com"
PORT = 5432
DATABASE_DB = "vet_app_db"

SQLALCHEMY_DATABASE_URL = f"{ENGINE_DB}://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT}/{DATABASE_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
