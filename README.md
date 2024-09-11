# Coffee-Shop

Welcome to the Coffee Shop Project! This application manages customers, coffees, and orders in a coffee shop setting. It allows you to create customers, manage coffee types, and place orders while keeping track of various statistics.

Features

Customer Management: Create and manage customer profiles.
Coffee Management: Add and manage different coffee types.
Order Management: Create orders linking customers and coffee.
Statistics: Calculate the number of orders and average prices for each coffee.
Advanced Features: Determine the most frequent 

Scenario:

You are tasked with building a domain model for a Coffee Shop. Your model will consist of three main entities: `Customer`, `Coffee`, and `Order`. The relationships are as follows:

- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.

The `Customer` and `Coffee` entities have a many-to-many relationship through the `Order` entity.

####Classes Overview
1. Customer Class (customer.py)
The Customer class represents a customer at the coffee shop. It includes the following attributes and methods:

Attributes:
name: A string representing the customer's name (between 1 and 15 characters).

Methods:
__init__(self, name): Initializes a Customer instance with a valid name.
orders(self): Returns a list of all orders associated with this customer.
coffees(self): Returns a unique list of coffee types that this customer has ordered.
create_order(self, coffee, price): Creates a new order for the customer with the given coffee and price.
most_aficionado(coffee): A class method that returns the customer who has spent the most on the given coffee type.
Validation:
Raises exceptions for invalid input (e.g., name exceeding 15 characters or non-string names).


2. Coffee Class (coffee.py)
The Coffee class represents a coffee item available at the shop. It includes attributes and methods for managing coffee-specific data.

Attributes:
name: A string representing the name of the coffee (must be at least 3 characters long).

Methods:
__init__(self, name): Initializes a Coffee instance with a valid name.
orders(self): Returns a list of all orders for this coffee.
customers(self): Returns a unique list of customers who have ordered this coffee.
num_orders(self): Returns the total number of orders for this coffee.
average_price(self): Returns the average price of all orders for this coffee.
Validation:
Raises exceptions for invalid coffee names (e.g., name shorter than 3 characters).

3. Order Class (order.py)
The Order class ties together a Customer and a Coffee, along with the price of the order.

Attributes:
customer: A Customer instance associated with this order.
coffee: A Coffee instance for the ordered coffee.
price: A float representing the price of the order 

Methods:
__init__(self, customer, coffee, price): Initializes an order with a valid Customer, Coffee, and price.
customer(self): Returns the Customer instance for the order.
coffee(self): Returns the Coffee instance for the order.



#####Unit Tests
Unit tests are included in the tests directory to ensure that the classes work as expected. We use pytest to run the tests. Below is an overview of the test files and the corresponding tests.

1. test_customer.py
This test file contains test cases for the Customer class.

Test Cases:

Test customer creation: Ensures that a customer can be created with a valid name.
Test invalid customer names: Tests that creating a customer with a name exceeding 15 characters or an invalid type raises an exception.
Test customer orders: Ensures that a customer can create an order and retrieve their list of orders.
Test customer coffees: Verifies that the coffees() method returns a unique list of coffees ordered by the customer.

2. test_coffee.py
This test file contains test cases for the Coffee class.

Test Cases:

Test coffee creation: Ensures that a coffee can be created with a valid name.
Test invalid coffee names: Tests that creating a coffee with a name shorter than 3 characters raises an exception.
Test coffee orders: Verifies that the orders() method returns all orders for a specific coffee.
Test coffee customers: Ensures that the customers() method returns a unique list of customers who have ordered the coffee.
Test num_orders and average_price: Verifies the calculation of total orders and average price for a coffee.

3. test_order.py

This test file contains test cases for the Order class.

Test Cases:
Test order creation: Ensures that an order can be created with a valid Customer, Coffee, and price.
Test invalid prices: Verifies that creating an order with an invalid price (less than 1.0 or greater than 10.0) raises an exception.
Test customer and coffee access: Ensures that the customer and coffee properties return the correct instances for an order.

#### CONTACTS

Any challenge you may contact me farida.mutai@student.moringaschool.com
