class Order:
    pass  # Define Order class as needed

class Coffee:
    pass  # Define Coffee class as needed

class Customer:
    _all_orders = []  # Class variable to keep track of all orders

    def __init__(self, name):
        self.name = name

    def add_order(self, order):
        Customer._all_orders.append(order)

    def orders(self):
        return [order for order in Customer._all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
