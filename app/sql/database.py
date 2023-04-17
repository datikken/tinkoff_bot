from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings import settings
from app.sql.models import Base

SQLALCHEMY_DATABASE_URL = f"mysql://{settings.db_user}:{settings.db_pass}@127.0.0.1:3306/{settings.db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

db = SessionLocal()
