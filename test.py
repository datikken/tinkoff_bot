from app.stats.sql_client import StatsSQLClient

client = StatsSQLClient()
  
client.update_order_status(123, 'bro')


orders = client.get_orders()

for order in orders:
    print(order.order_id, order.status)

