import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_creation():
    coffee = Coffee("Latte", "Medium", 5.0)
    assert coffee.name == "Latte"
    assert coffee.size == "Medium"
    assert coffee.price == 5.0

def test_invalid_coffee_name():
    with pytest.raises(ValueError):
        Coffee("Es", "Small", 3.0)

def test_num_orders():
    coffee = Coffee("Espresso", "Small", 3.0)
    customer = Customer("Alice", "alice@example.com")
    customer.create_order(coffee, 3.0)
    
    assert coffee.num_orders() == 1

def test_average_price():
    coffee = Coffee("Latte", "Medium", 5.0)
    customer1 = Customer("Alice", "alice@example.com")
    customer2 = Customer("Bob", "bob@example.com")
    
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 7.0)
    
    assert coffee.average_price() == 6.0
