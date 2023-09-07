# Phase3-final-project

This is a simple restaurant management system implemented in Python using SQLAlchemy, a popular Object Relational Mapping (ORM) library. The system allows you to manage users, food items, shopping carts, and orders.

# Table of Contents

Installation
Usage
Database Schema
Dependencies
Installation

# Clone this repository to your local machine:

git clone https://github.com/mukasa36/phase3-final-project.git

# Navigate to the project directory:
cd phase3-final-project

# Install the required dependencies:

pip install sqlalchemy

# Create the SQLite database:
python create_database.py

# Usage

To use this restaurant management system, you can import the modules.py file in your Python application and interact with the database using SQLAlchemy's ORM features.

Here is an example of how you can create a user, food items, and manage shopping carts and orders:

# Import necessary modules
from modules import Base, User, FoodItem, CartItem, Order, OrderItem, Session

# Create a SQLAlchemy engine and session
engine = create_engine('sqlite:///restaurant.db')
Base.metadata.create_all(engine)
session = Session()

# Create a new user
new_user = User(username="john_doe", password="password123")
session.add(new_user)
session.commit()

# Add food items
item1 = FoodItem(name="Burger", description="Delicious burger", price=10.99)
item2 = FoodItem(name="Pizza", description="Margherita pizza", price=12.99)
session.add_all([item1, item2])
session.commit()

# Create a shopping cart for the user
cart_item1 = CartItem(user=new_user, food_item=item1, quantity=2)
cart_item2 = CartItem(user=new_user, food_item=item2, quantity=1)
session.add_all([cart_item1, cart_item2])
session.commit()

# Place an order
order = Order(user=new_user, total_amount=cart_item1.food_item.price * cart_item1.quantity + cart_item2.food_item.price * cart_item2.quantity)
session.add(order)
session.commit()
You can customize and extend the functionality of this system according to your requirements.

# Database Schema
The system uses the following database tables and relationships:

users: Stores user information, including their username and password.
food_items: Contains details of food items, including name, description, and price.
cart_items: Represents items added to a user's shopping cart, with a reference to the user and food item, along with the quantity.
orders: Stores information about user orders, including the order date and total amount.
order_items: Represents individual items within an order, with references to the order, food item, quantity, and subtotal.
Dependencies
SQLAlchemy: A powerful and flexible ORM library for Python that simplifies database interactions.
Feel free to explore and modify the code to suit your specific needs for managing a restaurant's backend system.