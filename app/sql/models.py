from sqlalchemy import Column, Integer, String, Float
from app.sql.database import Base


class Order(Base):
  __tablename__ = 'orders'
  
  id = Column(Integer, primary_key=True, index=True)
  order_id = Column(String)
  figi = Column(String)
  order_direction = Column(String)
  price = Column(Float)
  quantity = Column(Integer)
  status = Column(String)