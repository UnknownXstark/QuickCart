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

class Product:
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

class OrderStatus(Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    DELIVERED = "Delivered"

class Order:
    def __init__(self, user, product, quantity):
        self.user = user
        self.product = product
        self.quantity = quantity
        self.status = OrderStatus.PENDING
        self.timestamp = datetime.now()
        self.rider = None

class Rider(User):
    def __init__(self, username, password, role=Role.USER):
        super().__init__(username, password, role.RIDER)
        self.assigned_orders = []