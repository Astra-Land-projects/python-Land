from inventory import InventoryManager

manager = InventoryManager()

while True:
    print("\n===== INVENTORY MANAGEMENT =====")
    print("1. Add Item")
    print("2. Show Inventory")
    print("3. Update Quantity")
    print("4. Delete Item")
    print("5. Exit")

    choice = input("Select: ")

    if choice == "1":
        name = input("Item Name: ")
        quantity = int(input("Quantity: "))
        manager.add_item(name, quantity)

    elif choice == "2":
        manager.show_items()

    elif choice == "3":
        index = int(input("Item Number: "))
        quantity = int(input("New Quantity: "))
        manager.update_quantity(index - 1, quantity)

    elif choice == "4":
        index = int(input("Item Number: "))
        manager.delete_item(index - 1)

    elif choice == "5":
        break

    else:
        print("Invalid Option")