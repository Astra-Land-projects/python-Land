# project_179_contact_book.py

contacts = []

while True:
    print("\n1. Add")
    print("2. Search")
    print("3. Show all")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        contacts.append({"name": name, "phone": phone})

    elif choice == "2":
        q = input("Search name: ").lower()
        results = [c for c in contacts if q in c["name"].lower()]
        for c in results:
            print(c["name"], "-", c["phone"])

    elif choice == "3":
        for c in contacts:
            print(c["name"], "-", c["phone"])

    elif choice == "4":
        break