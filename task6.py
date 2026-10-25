
# Smart Canteen Order and Stock Management

menu = {
    "Idli": {"price": 30, "stock": 20},
    "Dosa": {"price": 50, "stock": 15},
    "Vada": {"price": 20, "stock": 25},
    "Meals": {"price": 80, "stock": 10},
    "Tea": {"price": 10, "stock": 30}
}

total_sales = 0
total_orders = 0

def display_menu():
    print("\n--- CANTEEN MENU ---")
    print(f"{'Item':<10}{'Price':<10}{'Stock':<10}")
    for item, details in menu.items():
        print(
            f"{item:<10}"
            f"Rs.{details['price']:<7}"
            f"{details['stock']}"
        )

def place_order():
    global total_sales, total_orders

    bill = 0
    ordered_items = 0

    while True:
        display_menu()
        item = input(
            "\nEnter item name (or 'done' to finish): "
        ).strip().title()

        if item == "Done":
            break

        if item not in menu:
            print("Invalid item! Please select from the menu.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if quantity > menu[item]["stock"]:
            print("Sorry! Insufficient stock available.")
            print("Available quantity:", menu[item]["stock"])
            continue

        cost = menu[item]["price"] * quantity
        menu[item]["stock"] -= quantity
        bill += cost
        ordered_items += quantity

        print(f"{item} x {quantity} = Rs.{cost}")

    if ordered_items > 0:
        total_sales += bill
        total_orders += 1
        print("\n--- CUSTOMER BILL ---")
        print("Total items:", ordered_items)
        print("Total amount: Rs.", bill)
        print("Thank you! Visit again.")
    else:
        print("No items ordered.")

def daily_report():
    print("\n--- DAILY SALES REPORT ---")
    print("Completed customer orders:", total_orders)
    print("Total sales: Rs.", total_sales)

    print("\n--- REMAINING STOCK ---")
    for item, details in menu.items():
        print(f"{item}: {details['stock']} units")

while True:
    print("\n===== SMART CANTEEN SYSTEM =====")
    print("1. Display Menu")
    print("2. Place Customer Order")
    print("3. Daily Sales Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_menu()
    elif choice == "2":
        place_order()
    elif choice == "3":
        daily_report()
    elif choice == "4":
        print("Thank you for using the system!")
        daily_report()
        break
    else:
        print("Invalid choice. Please try again.")
