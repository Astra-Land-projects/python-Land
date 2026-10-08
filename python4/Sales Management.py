from sales import SalesManager

manager = SalesManager()

while True:
    print("\n===== SALES MANAGEMENT =====")
    print("1. Add Product")
    print("2. Show Products")
    print("3. Sell Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Select: ")

    if choice == "1":
        name = input("Product Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        manager.add_product(name, price, quantity)

    elif choice == "2":
        manager.show_products()

    elif choice == "3":
        index = int(input("Product Number: "))
        qty = int(input("Quantity: "))
        manager.sell_product(index - 1, qty)

    elif choice == "4":
        index = int(input("Product Number: "))
        manager.delete_product(index - 1)

    elif choice == "5":
        break

    else:
        print("Invalid Option")