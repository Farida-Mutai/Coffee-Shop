import pytest
from coffee import Coffee  
from customer import Customer  
from order import Order  

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("A" * 16)
    Customer("ValidName")



def test_customer_create_order():
    customer = Customer("Mutai")
    order = customer.create_order("Mocha", 3.5)
    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == "Mocha"
    assert order.price == 3.5

def test_customer_orders():
    customer = Customer("Mutai")
    order1 = Order(customer, "Mocha", 3.5)
    order2 = Order(customer, "Cold Brew", 4.0)
    assert customer.orders() == [order1, order2]

def test_customer_coffees():
    customer = Customer("Mutai")
    order1 = Order(customer, "Mocha", 3.5)
    order2 = Order(customer, "Cold Brew", 4.0)
    assert customer.coffees() == {"Mocha", "Cold Brew"}

def test_customer_most_aficionado():
    customer1 = Customer("Mutai")
    customer2 = Customer("Mutai")
    order1 = Order(customer1, "Mocha", 3.5)
    order2 = Order(customer2, "Mocha", 4.0)
    assert Customer.most_aficionado("Mocha") == customer2