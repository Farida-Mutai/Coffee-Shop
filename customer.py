class Customer:
    def __init__(self, name, email, phone_number=None):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.orders = []  # List to store the customer's orders

    def place_order(self, order):
        """Add an order to the customer's order history."""
        self.orders.append(order)

    def get_order_history(self):
        """Return a list of all past orders."""
        return self.orders

    def __repr__(self):
        return f"Customer({self.name}, {self.email})"
