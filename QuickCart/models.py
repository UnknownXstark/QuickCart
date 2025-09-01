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