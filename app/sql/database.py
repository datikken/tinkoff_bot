from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.settings import settings


SQLALCHEMY_DATABASE_URL = f"mysql://{settings.db_user}:{settings.db_pass}@127.0.0.1:3306/{settings.db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

db = SessionLocal()
