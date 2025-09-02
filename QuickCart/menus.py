from services import *

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