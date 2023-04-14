from sqlalchemy import Column, Integer, String, Float
from app.sql.database import Base


class Order(Base):
  __tablename__ = 'orders'
  
  id = Column(Integer, primary_key=True, index=True)
  order_id = Column(String(256))
  figi = Column(String(256))
  order_direction = Column(String(256))
  price = Column(Float)
  quantity = Column(Integer)
  status = Column(String(256))
