from sqlalchemy import create_engine
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./sql_app.sqlite"
# DATABASE_URL = "postgresql://user:pass@localhost/tinyurl"

engine = create_engine(
    DATABASE_URL, connect_args=dict(check_same_thread=False)
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

