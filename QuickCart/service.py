from models import User, Rider, Product, Order, Role

users = []
products = []
orders = []

def register(username, password, role=Role.USER):
    if any(u.username == username for u in users):
        return None
    if role == Role.RIDER:
        