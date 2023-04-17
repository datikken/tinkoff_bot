from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.settings import settings
from sqlalchemy import Column, Integer, String, Float

SQLALCHEMY_DATABASE_URL = f"mysql://{settings.db_user}:{settings.db_pass}@127.0.0.1:3306/{settings.db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Order(Base):
  __tablename__ = 'orders'
  
  id = Column(Integer, primary_key=True, index=True)
  order_id = Column(String(256))
  figi = Column(String(256))
  order_direction = Column(String(256))
  price = Column(Float)
  quantity = Column(Integer)
  status = Column(String(256))


Base.metadata.create_all(bind=engine)

db = SessionLocal()
