from models import User, Rider, Product, Order, Role

users = []
products = []
orders = []

def register(username, password, role=Role.USER):
    if any(u.username == username for u in users):
        return None
    if role == Role.RIDER:
        user = Rider(username, password)
    else:
        user = User(username, password, role)
        users.append(user)
        return user
    
def login(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user
        return None
    
def add_product(name, price, stock):
    product = Product(name, price, stock)
    products.append(product)
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
            return order
        return None