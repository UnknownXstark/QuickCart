from enum import Enum
from datetime import datetime

class Role(Enum):
    ADMIN = "Admin"
    USER = "User"
    RIDER = "Rider"

class User:
    def __init__(self, username, password, role=Role.USER):
        self.username = username
        self.password = password
        self.role = role
        self.orders = []
    
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role.value,
        }
    
    @classmethod
    def from_dict(cls, data):
        role = Role(data["role"])
        user = cls(data["username"], data["password"], role)
        return user

class Product:
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"], data["stock"])

class OrderStatus(Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    DELIVERED = "Delivered"

class Order:
    def __init__(self, user, product, quantity):
        self.user = user.username if isinstance(user, User) else user
        self.product = product.name if isinstance(product, Product) else product
        self.quantity = quantity
        self.status = OrderStatus.PENDING
        self.timestamp = datetime.now().isoformat()
        self.rider = None

    def to_dict(self):
        return {
            "user": self.user,
            "product": self.product,
            "quantity": self.quantity,
            "status": self.status.value,
            "timestamp": self.timestamp,
            "rider": self.rider if not isinstance(self.rider, User) else self.rider.username
        }
    
    @classmethod
    def from_dict(cls, data):
        order = cls(data["user"], data["product"], data["quantity"])
        order.status = OrderStatus(data["status"])
        order.timestamp = data["timestamp"]
        order.rider = data["rider"]
        return order

class Rider(User):
    def __init__(self, username, password, role=Role.RIDER):
        super().__init__(username, password, role)
        self.assigned_orders = []

    def to_dict(self):
        return super().to_dict()
    
    @classmethod
    def from_dict(cls, data):
        rider = cls(data["username"], data["password"])
        return rider