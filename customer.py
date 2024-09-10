# customer.py

from order import Order
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

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

class Customer:
    _all_orders = []  # Class variable to keep track of all orders

    def __init__(self, name):
        self.name = name

    def create_order(self, coffee, price):
        order = Order(customer=self, coffee=coffee, price=price)
        Customer._all_orders.append(order)
        coffee.add_order(order)
        return order

    def orders(self):
        return [order for order in Customer._all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    @classmethod
    def most_aficionado(cls, coffee):
        customer_spending = {}
        
        # Iterate over all orders
        for order in cls._all_orders:
            if order.coffee == coffee:
                if order.customer not in customer_spending:
                    customer_spending[order.customer] = 0
                customer_spending[order.customer] += order.price
        
        # Determine the customer who spent the most
        if customer_spending:
            most_spent_customer = max(customer_spending, key=customer_spending.get)
            return most_spent_customer
        
        return None
