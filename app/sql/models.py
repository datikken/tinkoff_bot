from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

now = datetime.datetime.utcnow

class Order(Base):
  __tablename__ = 'orders'
  __table_args__ = {'extend_existing': True}

  id = Column(Integer, primary_key=True, index=True)
  order_id = Column(String(256))
  figi = Column(String(256))
  order_direction = Column(String(256))
  price = Column(Float)
  quantity = Column(Integer)
  status = Column(String(256))


class Corridor(Base):
  __tablename__ = 'corridors'
  __table_args__ = {'extend_existing': True}

  id = Column(Integer, primary_key=True, index=True)
  bottom = Column(Float)
  top = Column(Float)
  current = Column(Float)
  days_considered = Column(Integer)
  figi = Column(String(256))
  created_at = Column(DateTime, default=now)
  updated_at = Column(DateTime, default=now)