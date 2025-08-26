from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


SQLITE_DATABASE_URI = "sqlite:///./instagram_api.db"

engine = create_engine(SQLITE_DATABASE_URI, connect_args= {'check_same_thread' : False})

SessionLocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()