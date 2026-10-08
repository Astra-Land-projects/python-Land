database = []

while True:
    print("\n1 Insert")
    print("2 Find")
    print("3 Show")
    print("4 Exit")

    choice = input("> ")

    if choice == "1":
        record = input("Data: ")
        database.append(record)

    elif choice == "2":
        query = input("Search: ").lower()

        for record in database:
            if query in record.lower():
                print(record)

    elif choice == "3":
        for record in database:
            print(record)

    elif choice == "4":
        break