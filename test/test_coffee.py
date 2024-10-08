import pytest
from coffee import Coffee
from order import Order  
from customer import Customer  

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("A" * 16)
    Customer("ValidName")


def test_coffee_orders():
    coffee = Coffee("Coffee")
    customer1 = Customer("Lynn")
    customer2 = Customer("Mutai")
    order1 = Order(customer1, coffee, 3.5)
    order2 = Order(customer2, coffee, 4.0)
    assert coffee.orders() == [order1, order2]

def test_coffee_customers():
    coffee = Coffee("Coffee")
    customer1 = Customer("Lynn")
    customer2 = Customer("Mutai")
    order1 = Order(customer1, coffee, 3.5)
    order2 = Order(customer2, coffee, 4.0)
    assert coffee.customers() == {customer1, customer2}

def test_coffee_num_orders():
    coffee = Coffee("Coffee")
    customer = Customer("Lynn")
    order1 = Order(customer, coffee, 3.5)
    order2 = Order(customer, coffee, 4.0)
    assert coffee.num_orders() == 2

def test_coffee_average_price():
    coffee = Coffee("Coffee")
    customer = Customer("Lynn")
    order1 = Order(customer, coffee, 3.5)
    order2 = Order(customer, coffee, 4.0)
    assert coffee.average_price() == 3.75