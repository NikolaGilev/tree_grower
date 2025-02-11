import os

from sqlmodel import SQLModel, create_engine, Session

# from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL
from dotenv import load_dotenv

load_dotenv(override=True)

POSTGRES_URL = os.getenv("POSTGRES_URL")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")


database_url = url = URL.create(
    drivername="postgresql",
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_URL,
    database=POSTGRES_DATABASE,
    port=5432,
)
engine = create_engine(database_url, echo=True)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
