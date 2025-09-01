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

class Order:
    def __init__(self, order_id,  user_id, product, quantity):
        self.order_id = order_id
        self.user_id = user_id
        self.product = product
        self.quantity = quantity
        self.status = OrderStatus.PENDING
    
    def __str__(self):
        return f"{self.order_id}: {self.product.name}"