from models import User, Rider, Product, Order, Role, OrderStatus
from storage import load_data, save_data

# Load users, handling riders correctly
users_data = load_data("users.json")
users = []
for u_data in users_data:
    role = Role(u_data["role"])
    if role == Role.RIDER:
        user = Rider.from_dict(u_data)
    else:
        user = User.from_dict(u_data)
    users.append(user)

products = [Product.from_dict(p) for p in load_data("products.json")]
orders = [Order.from_dict(o) for o in load_data("orders.json")]

# Link orders to users and riders
for order in orders:
    for user in users:
        if user.username == order.user:
            user.orders.append(order)
            break
    if order.rider:
        for user in users:
            if user.username == order.rider and isinstance(user, Rider):
                user.assigned_orders.append(order)
                break

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
    if order.status == OrderStatus.PENDING:
        order.status = OrderStatus.ACCEPTED
        order.rider = rider.username
        rider.assigned_orders.append(order)
        save_all()
        return True
    return False

def rider_deliver_order(rider, order):
    if order in rider.assigned_orders and order.status == OrderStatus.ACCEPTED:
        order.status = OrderStatus.DELIVERED
        save_all()
        return True
    return False