from enum import Enum
import uuid

class OrderStatus(Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    DELIVERED = "Delivered"

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (stock: {self.stock})"

