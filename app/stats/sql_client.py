from app.sql.models import Order
from app.sql.database import db


class StatsSQLClient:
    def save(self):
        db.flush()
        db.commit()

    def add_order(
        self,
        order_id: str,
        figi: str,
        order_direction: str,
        price: float,
        quantity: int,
        status: str,
    ):
      order = Order(
          order_id=order_id,
          figi=figi,
          order_direction=order_direction,
          price=price,
          quantity=quantity,
          status=status
      )
      db.add(order)
      self.save()

    def get_orders(self):
        return db.query(Order).all()

    def update_order_status(self, order_id: str, status: str):
        db.query(Order).filter(Order.order_id ==
                               order_id).update({Order.status: status})
        self.save()
