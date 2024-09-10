
class Coffee:
    def __init__(self, name, size, price, ingredients=[]):
        self.name = name
        self.size = size
        self.price = price
        self.ingredients = ingredients

    def calculate_price(self):
        """Calculate the price of the coffee, which may vary by size and ingredients."""
        return self.price

    def describe_coffee(self):
        """Return a string description of the coffee."""
        ingredients_str = ', '.join(self.ingredients)
        return f"{self.size} {self.name} with {ingredients_str} - ${self.price}"

    def __repr__(self):
        return f"Coffee({self.name}, {self.size}, ${self.price})"
