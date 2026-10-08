from notes import NotesApp

app = NotesApp()

while True:
    print("\n===== NOTES APP =====")
    print("1. Add Note")
    print("2. Show Notes")
    print("3. Delete Note")
    print("4. Exit")

    choice = input("Select: ")

    if choice == "1":
        note = input("Write Note: ")
        app.add_note(note)

    elif choice == "2":
        app.show_notes()

    elif choice == "3":
        index = int(input("Note Number: "))
        app.delete_note(index - 1)

    elif choice == "4":
        print("Bye 👋")
        break

    else:
        print("Invalid Option!")