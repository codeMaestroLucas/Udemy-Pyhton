from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_PATH = ROOT_DIR / 'database.db'
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine: Engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args= {"check_same_thread": False},
    # echo= True
)

LocalSession = sessionmaker(autocommit= False, autoflush= False, bind= engine)

Base = declarative_base()

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
