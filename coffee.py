class Coffee:
    def __init__(self, name, size, price, ingredients=[]):
        self._name = None  # Placeholder for name validation
        self.name = name  # Triggers the setter for validation
        self.size = size
        self.price = price
        self.ingredients = ingredients

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be at least 3 characters long.")

    def calculate_price(self):
        return self.price

    def describe_coffee(self):
        ingredients_str = ', '.join(self.ingredients)
        return f"{self.size} {self.name} with {ingredients_str} - ${self.price}"

    def __repr__(self):
        return f"Coffee({self.name}, {self.size}, ${self.price})"
