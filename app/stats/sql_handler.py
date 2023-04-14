from app.sql.models import Order
from app.sql.database import db

# order = Order(order_id='123', figi='figi', order_direction='top', price=1.2, quantity=1, status='pre')

# db.add(order)
# db.flush()
# db.commit()

orders = db.query(Order).all()

for item in orders:
    print(item.order_id)
    print(item.price)