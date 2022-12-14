from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URI = "sqlite;//example.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args = {"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

