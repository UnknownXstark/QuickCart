from service import register, login
from menus import admin_menu, user_menu, riders_menu
from models import Role

register("admin", "admin", Role.ADMIN)

while True:
    print("\n--- QuickCart ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        role_choice = input("Role (user/rider): ").lower()
        role = Role.USER if role_choice == "User" else Role.RIDER
        user = register(username, password, role)
        if user:
            print("Registered succesfully!")
        else:
            print("Username already exists.")
    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        user = login(username, password)
        if not user:
            print("Invalid credentials.")
        else:
            if user.role == Role.ADMIN:
                admin_menu(user)
            elif user.role == Role.USER:
                user_menu(user)
            elif user.role == Role.RIDER:
                rider_menu