class Order:
    order_id_counter = 1

    def __init__(self, customer, coffee):
        self._customer = None  # Placeholder for customer validation
        self._coffee = None    # Placeholder for coffee validation
        self._price = None     # Placeholder for price validation
        
        self.customer = customer  # Triggers the setter for validation
        self.coffee = coffee      # Triggers the setter for validation
        self.price = coffee.price # Price is automatically set based on the coffee instance
        
        self.order_id = Order.order_id_counter
        Order.order_id_counter += 1
        self.coffee_list = [coffee]
        self.total_price = coffee.price
        self.status = "pending"

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("Customer must be an instance of the Customer class.")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("Coffee must be an instance of the Coffee class.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")

    def add_coffee(self, coffee):
        self.coffee_list.append(coffee)
        self.calculate_total()

    def remove_coffee(self, coffee):
        if coffee in self.coffee_list:
            self.coffee_list.remove(coffee)
            self.calculate_total()

    def calculate_total(self):
        self.total_price = sum(coffee.calculate_price() for coffee in self.coffee_list)

    def update_status(self, new_status):
        self.status = new_status

    def __repr__(self):
        return f"Order({self.order_id}, Customer: {self.customer.name}, Total: ${self.total_price})"
