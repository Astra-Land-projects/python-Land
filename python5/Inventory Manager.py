inventory = {}

while True:
    print("\n1 Add")
    print("2 Remove")
    print("3 Show")
    print("4 Exit")

    choice = input("> ")

    if choice == "1":
        name = input("Product: ")
        amount = int(input("Quantity: "))
        inventory[name] = inventory.get(name, 0) + amount

    elif choice == "2":
        name = input("Product: ")
        amount = int(input("Quantity: "))

        if name in inventory:
            inventory[name] = max(0, inventory[name] - amount)

    elif choice == "3":
        for name, amount in inventory.items():
            print(name, ":", amount)

    elif choice == "4":
        break