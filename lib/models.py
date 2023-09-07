from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

class FoodItem(Base):
    __tablename__ = 'food_items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    order_date = Column( default=datetime.datetime.utcnow)
    total_amount = Column(Float)

    user = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    food_id = Column(Integer, ForeignKey('food_items.id'))
    quantity = Column(Integer)
    subtotal = Column(Float)

    order = relationship("Order", back_populates="order_items")
    food_item = relationship("FoodItem")

def create_database():
    # Create a SQLAlchemy engine and session
    engine = create_engine('sqlite:///finalproject.db')

    # Check if the database already exists
    if not engine.dialect.has_table(engine, User.__tablename__):
        Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)

    # Add relationships to User and FoodItem
    User.orders = relationship("Order", back_populates="user")
    FoodItem.order_items = relationship("OrderItem", back_populates="food_item")

if __name__ == "__main__":
    create_database()
