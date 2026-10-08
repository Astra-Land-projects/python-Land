balance = 0

while True:
    print("\n1 Deposit")
    print("2 Withdraw")
    print("3 Balance")
    print("4 Exit")

    choice = input("> ")

    if choice == "1":
        amount = float(input("Amount: "))
        balance += amount

    elif choice == "2":
        amount = float(input("Amount: "))

        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient balance")

    elif choice == "3":
        print("Balance:", balance)

    elif choice == "4":
        break