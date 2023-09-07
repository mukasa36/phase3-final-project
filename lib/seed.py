import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, FoodItem, Order, OrderItem

if __name__ == '__main__':
    engine = create_engine('sqlite:////home/emmanuel/Development/code/phase3/phase3-final-project/finalproject.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    session.query(FoodItem).delete()
    session.query(Order).delete()
    session.query(OrderItem).delete()

# fake = Faker()

from models import User, FoodItem, Order, OrderItem, Session

# Create a session
session = Session()

# Add sample data

# Users
user1 = User(username='john_doe', password='password123')
user2 = User(username='jane_smith', password='password456')
session.add_all([user1, user2])

# Food Items
food1 = FoodItem(name='Spaghetti Bolognese', description='Classic Italian dish', price=12.99)
food2 = FoodItem(name='Chicken Alfredo', description='Creamy pasta with chicken', price=14.99)
food3 = FoodItem(name='Caesar Salad', description='Fresh Caesar salad', price=7.99)
food4 = FoodItem(name='Cheeseburger', description='Juicy cheeseburger', price=9.99)
session.add_all([food1, food2, food3, food4])

# Orders
order1 = Order(user=user1, total_amount=food1.price + food3.price)
order2 = Order(user=user2, total_amount=food4.price)
session.add_all([order1, order2])

# Order Items
order_item1 = OrderItem(order=order1, food_item=food1, quantity=1, subtotal=food1.price)
order_item2 = OrderItem(order=order1, food_item=food3, quantity=1, subtotal=food3.price)
order_item3 = OrderItem(order=order2, food_item=food4, quantity=1, subtotal=food4.price)
session.add_all([order_item1, order_item2, order_item3])

# Commit the changes to the database
session.commit()

# Close the session
session.close()

print("Sample data has been added to the database.")

