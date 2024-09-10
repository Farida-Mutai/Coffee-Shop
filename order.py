class Customer:
    pass  # Define Customer class as needed

class Coffee:
    pass  # Define Coffee class as needed

class Order:
    def __init__(self, customer, coffee):
        self.customer = customer
        self.coffee = coffee

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        self._coffee = coffee
