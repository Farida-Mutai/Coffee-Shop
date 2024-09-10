# coffee.py

from customer import Order

class Coffee:
    _all_orders = []  # Class variable to keep track of all orders

    def __init__(self, name):
        self.name = name

    def add_order(self, order):
        Coffee._all_orders.append(order)

    def num_orders(self):
        return len([order for order in Coffee._all_orders if order.coffee == self])

    def average_price(self):
        orders = [order for order in Coffee._all_orders if order.coffee == self]
        if orders:
            total_price = sum(order.price for order in orders)
            return total_price / len(orders)
        return 0.0
