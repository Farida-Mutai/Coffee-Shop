class Order:
    pass  # Define Order class as needed

class Coffee:
    _all_orders = []  # Class variable to keep track of all orders

    def __init__(self, name):
        self.name = name

    def add_order(self, order):
        Coffee._all_orders.append(order)

    def orders(self):
        return [order for order in Coffee._all_orders if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))
