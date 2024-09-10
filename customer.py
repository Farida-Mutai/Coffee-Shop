class Customer:
    def __init__(self, name, email, phone_number=None):
        self._name = None  # Placeholder for name validation
        self.name = name  # Triggers the setter for validation
        self.email = email
        self.phone_number = phone_number
        self.orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def place_order(self, order):
        self.orders.append(order)

    def get_order_history(self):
        return self.orders

    def __repr__(self):
        return f"Customer({self.name}, {self.email})"
