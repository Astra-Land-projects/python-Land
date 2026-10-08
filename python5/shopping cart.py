cart = []

while True:
    print("\n1 Add item")
    print("2 Show cart")
    print("3 Total")
    print("4 Exit")

    choice = input("> ")

    if choice == "1":
        name = input("Item: ")
        price = float(input("Price: "))
        cart.append((name, price))

    elif choice == "2":
        for name, price in cart:
            print(name, "-", price)

    elif choice == "3":
        print("Total:", sum(price for _, price in cart))

    elif choice == "4":
        break