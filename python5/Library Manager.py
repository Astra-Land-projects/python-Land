books = {
    "Python": True,
    "Clean Code": True,
    "Deep Learning": True
}

while True:
    print("\n1 Show books")
    print("2 Borrow")
    print("3 Return")
    print("4 Exit")

    choice = input("> ")

    if choice == "1":
        for book, available in books.items():
            print(book, "Available" if available else "Borrowed")

    elif choice == "2":
        book = input("Book: ")
        if book in books and books[book]:
            books[book] = False

    elif choice == "3":
        book = input("Book: ")
        if book in books:
            books[book] = True

    elif choice == "4":
        break