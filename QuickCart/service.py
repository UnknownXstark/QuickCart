from models import User, Rider, Product, Order, Role
from storage import load_data, save_data

users = [User(**u) for u in load_data("users.json")]
products = [Product(**p) for p in load_data("products.json")]
orders = [Order(**o) for o in load_data("orders.json")]

def register(username, password, role=Role.USER):
    if any(u.username == username for u in users):
        return None
    if role == Role.RIDER:
        user = Rider(username, password)
    else:
        user = User(username, password, role)
    users.append(user)
    save_data([u.__dict__ for u in users], "users.json")
    return user
    
def login(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None
    
def add_product(name, price, stock):
    product = Product(name, price, stock)
    products.append(product)
    save_data([p.__dict__ for p in products], "products.json")
    return product

def list_products():
    return products

def place_order(user, product_name, quantity):
    for product in products:
        if product.name == product_name and product.stock >= quantity:
            product.stock -= quantity
            order = Order(user, product, quantity)
            orders.append(order)
            user.orders.append(order)
            save_data([p.__dict__ for p in products], "products.json")
            save_data([o.__dict__ for o in orders], "orders.json")
            return order
    return None
    
def rider_accept_order(rider, order):
    if order.status == order.status.PENDING:
        order.status = order.status.ACCEPTED
        order.rider = rider
        rider.assigned_orders.append(order)
        save_data([o.__dict__ for o in orders], "orders.json")
        return True
    return False

def rider_deliver_order(rider, order):
    if order in rider.assigned_orders and order.status == order.status.ACCEPTED:
        order.status = order.status.DELIVERED
        save_data([o.__dict__ for o in orders], "orders.jsoon")
        return True
    return False