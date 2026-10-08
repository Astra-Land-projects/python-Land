from library import Library

library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Select: ")

    if choice == "1":
        title = input("Book Name: ")
        author = input("Author: ")
        library.add_book(title, author)

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        index = int(input("Book Number: "))
        library.borrow_book(index - 1)

    elif choice == "4":
        index = int(input("Book Number: "))
        library.return_book(index - 1)

    elif choice == "5":
        index = int(input("Book Number: "))
        library.delete_book(index - 1)

    elif choice == "6":
        break

    else:
        print("Invalid Option")