import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_creation():
    customer = Customer("Alice", "alice@example.com")
    coffee = Coffee("Latte", "Medium", 5.0)
    order = Order(customer, coffee)
    
    assert order.customer == customer
    assert order.coffee == coffee

def test_order_price_validation():
    customer = Customer("Alice", "alice@example.com")
    coffee = Coffee("Latte", "Medium", 5.0)
    
    with pytest.raises(ValueError):
        order = Order(customer, coffee, price=20.0)  # Invalid price, should raise an error
