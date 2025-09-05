from service import *
from models import OrderStatus

def admin_menu(admin):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Product")
        print("2. View Orders")
        print("3. Logout")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Product name: ")
            try:
                price = float(input("Price: "))
                stock = int(input("Stock: "))
                add_product(name, price, stock)
                print("Product added!")
            except ValueError:
                print("Invalid price or stock. Please enter numbers.")
        
        elif choice == "2":
            for o in orders:
                print(f"{o.user} ordered {o.quantity} {o.product} [{o.status.value}]")

        elif choice == "3":
            break

def user_menu(user):
    while True:
        print("\n--- User Menu ---")
        print("1. Browse Products")
        print("2. Place Order")
        print("3. My Orders")
        print("4. Logout")
        choice = input("Choose: ")

        if choice == "1":
            for p in list_products():
                print(f"{p.name} - ${p.price} (Stock: {p.stock})")
        
        elif choice == "2":
            name = input("Product name: ")
            try:
                qty = int(input("Quantity: "))
                order = place_order(user, name, qty)
                if order:
                    print("Order placed!")
                else:
                    print("Order failed (not enough stock or product not found).")
            except ValueError:
                print("Invalid quantity. Please enter a number.")

        elif choice == "3":
            for o in user.orders:
                print(f"{o.product} x{o.quantity} [{o.status.value}]")

        elif choice == "4":
            break

def rider_menu(rider):
    while True:
        print("\n--- Rider Menu ---")
        print("1. Accept Order")
        print("2. Deliver Order")
        print("3. My Orders")
        print("4. Logout")
        choice = input("Choose: ")

        if choice == "1":
            pending_orders = [o for o in orders if o.status == OrderStatus.PENDING]
            if not pending_orders:
                print("No pending orders.")
                continue
            for i, o in enumerate(pending_orders):
                print(f"{i}. {o.user} ordered {o.product} x{o.quantity}")
            try:
                idx = int(input("Choose order index: "))
                if 0 <= idx < len(pending_orders):
                    rider_accept_order(rider, pending_orders[idx])
                    print("Order accepted!")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == "2":
            accepted_orders = [o for o in rider.assigned_orders if o.status == OrderStatus.ACCEPTED]
            if not accepted_orders:
                print("No accepted orders to deliver.")
                continue
            for i, o in enumerate(accepted_orders):
                print(f"{i}. {o.product} for {o.user}")
            try:
                idx = int(input("Choose order index: "))
                if 0 <= idx < len(accepted_orders):
                    rider_deliver_order(rider, accepted_orders[idx])
                    print("Order delivered!")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "3":
            if not rider.assigned_orders:
                print("No assigned orders.")
                continue
            for o in rider.assigned_orders:
                print(f"{o.product} x{o.quantity} for {o.user} [{o.status.value}]")

        elif choice == "4":
            break