

# seed.py

from models import User, FoodItem, CartItem, Order, OrderItem, Session, engine

# Create database tables
User.metadata.create_all(engine)
FoodItem.metadata.create_all(engine)
CartItem.metadata.create_all(engine)
Order.metadata.create_all(engine)
OrderItem.metadata.create_all(engine)

# Create a session
session = Session()

# Add sample data

# Users
user1 = User(username='user1', password='password1')
user2 = User(username='user2', password='password2')
session.add_all([user1, user2])

# Food Items
food1 = FoodItem(name='Burger', description='Delicious burger', price=8.99)
food2 = FoodItem(name='Pizza', description='Margherita pizza', price=10.99)
food3 = FoodItem(name='Salad', description='Fresh garden salad', price=5.99)
session.add_all([food1, food2, food3])

# Cart Items
cart_item1 = CartItem(user=user1, food_item=food1, quantity=2)
cart_item2 = CartItem(user=user2, food_item=food2, quantity=1)
session.add_all([cart_item1, cart_item2])

# Orders
order1 = Order(user=user1, total_amount=cart_item1.food_item.price * cart_item1.quantity)
order2 = Order(user=user2, total_amount=cart_item2.food_item.price * cart_item2.quantity)
session.add_all([order1, order2])

# Order Items
order_item1 = OrderItem(order=order1, food_item=food1, quantity=cart_item1.quantity, subtotal=cart_item1.food_item.price * cart_item1.quantity)
order_item2 = OrderItem(order=order2, food_item=food2, quantity=cart_item2.quantity, subtotal=cart_item2.food_item.price * cart_item2.quantity)
session.add_all([order_item1, order_item2])

# Commit the changes to the database
session.commit()

# Close the session
session.close()

print("Sample data has been added to the database.")
