from models import User, Rider, Product, Order, Role
from storage import load_data, save_data

users = [User.from_dict(u) for u in load_data("users.json")]
products = [Product.from_dict(p) for p in load_data("products.json")]
orders = [Order.from_dict(o) for o in load_data("orders.json")]

def save_all():
    save_data([u.to_dict() for u in users], "users.json")
    save_data([p.to_dict() for p in products], "products.json")
    save_data([o.to_dict() for o in orders], "orders.json")

def register(username, password, role=Role.USER):
    if any(u.username == username for u in users):
        return None
    if role == Role.RIDER:
        user = Rider(username, password)
    else:
        user = User(username, password, role)
    users.append(user)
    save_all()
    return user
    
def login(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None
    
def add_product(name, price, stock):
    product = Product(name, price, stock)
    products.append(product)
    save_all()
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
            save_all()
            return order
    return None
    
def rider_accept_order(rider, order):
    if order.status == Order.status.PENDING:
        order.status = Order.status.ACCEPTED
        order.rider = rider
        rider.assigned_orders.append(order)
        save_all()
        return True
    return False

def rider_deliver_order(rider, order):
    if order in rider.assigned_orders and order.status == Order.status.ACCEPTED:
        order.status = order.status.DELIVERED
        save_all()
        return True
    return False