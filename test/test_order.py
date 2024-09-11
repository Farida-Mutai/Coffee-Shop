import pytest
from coffee import Coffee  
from order import Order 
from customer import Customer  

def test_order_price_validation():
    customer = Customer("Mutai")
    with pytest.raises(ValueError):
        Order(customer, "Mocha", 0.9)
    with pytest.raises(ValueError):
        Order(customer, "Mocha", 10.1)
    Order(customer, "Mocha", 5.0)

def test_order_properties():
    customer = Customer("Mutai")
    order = Order(customer, "Mocha", 3.5)
    assert order.customer == customer
    assert order.coffee == "Mocha"
    assert order.price == 3.5

def test_order_all_orders():
    customer1 = Customer("Mutai")
    customer2 = Customer("Lynn")
    order1 = Order(customer1, "Mocha", 3.5)
    order2 = Order(customer2, "Cold Brew", 4.0)
    