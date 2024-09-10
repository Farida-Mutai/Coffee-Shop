import pytest
from customer import Customer
from coffee import Coffee

def test_customer_creation():
    customer = Customer("Alice", "alice@example.com")
    assert customer.name == "Alice"
    assert customer.email == "alice@example.com"

def test_invalid_customer_name():
    with pytest.raises(ValueError):
        Customer("ThisNameIsWayTooLong", "test@example.com")

def test_create_order():
    customer = Customer("Alice", "alice@example.com")
    coffee = Coffee("Latte", "Medium", 5.0)
    order = customer.create_order(coffee, 5.0)
    assert order.price == 5.0
    assert order.customer == customer
    assert order.coffee == coffee

def test_most_aficionado():
    customer1 = Customer("Alice", "alice@example.com")
    customer2 = Customer("Bob", "bob@example.com")
    coffee = Coffee("Latte", "Medium", 5.0)
    
    customer1.create_order(coffee, 5.0)
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 10.0)
    
    assert Customer.most_aficionado(coffee) == customer1
