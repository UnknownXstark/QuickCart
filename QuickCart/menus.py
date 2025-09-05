from service import *

def admin_menu(admin):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Product")
        print("2. View Orders")
        print("3. Logout")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Product name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            add_product(name, price, stock)
            print("Product added!")
        elif choice == "2":
            for o in orders:
                print(f"{o.user.username} ordered {o.quantity} {o.product.name} [{o.status.value}]")
        elif choice == "3":
            break

def user_menu(user):
    while True:
        print("\n-- User Menu --")
        print("1. Browse Products")
        print("2. Place Orders")
        print("3. My Orders")
        print("4. Logout")
        choice = input("Choose: ")

        if choice == "1":
            for p in list_products():
                print(f"{p.name} - ${p.price} (Stock: {p.stock})")
        
        elif choice == "2":
            name = input("Product name: ")
            qty = int(input("Quantity: "))
            order = place_order(user, name, qty)
            if order:
                print("Order placed!")
            else:
                print("Order failed (not enough stock).")
        elif choice == "3":
            for o in user.orders:
                print(f"{o.product.name} x{o.quantity} [{o.status.value}]")
        elif choice == "4":
            break

def rider_menu(rider):
    while True:
        print("\n-- Riders Menu --")
        print("1. Accept Order")
        print("2. Deliver Order")
        print("3. My Orders")
        print("4. Logout")
        choice = input("Choose: ")

        if choice == "1":
            for i, o in enumerate(orders):
                if o.status == o.status.PENDING:
                    print(f"{i}.{o.user.username} ordered {o.producut.name} x{o.quantity}")
            idx = int(input("Choose order index: "))
            rider_accept_order(rider, orders[idx])
            print("Order accepted!")
        elif choice == "2":
            for i, o in enumerate(orders):
                if o.status == o.status.ACCEPTED:
                    print(f"{i}.{o.product.name} for {o.user.username}")
            idx = int(input("Choose order index: "))
            rider_deliver_order(rider, rider.assigned_orders[idx])
            print("Order delivered!")
        elif choice == "3":
            for o in rider.assigned_orders:
                print(f"{o.product.name} [{o.status.value}]")
        elif choice == "4":
            break