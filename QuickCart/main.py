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