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

