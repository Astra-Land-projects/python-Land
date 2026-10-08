from task_manager import TaskManager


def show_menu():
    print("\n===== TODO APP =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def main():
    manager = TaskManager()

    while True:
        show_menu()

        choice = input("Select: ")

        if choice == "1":
            title = input("Task: ")
            manager.add_task(title)

        elif choice == "2":
            manager.show_tasks()

        elif choice == "3":
            index = int(input("Task Number: "))
            manager.complete_task(index - 1)

        elif choice == "4":
            index = int(input("Task Number: "))
            manager.delete_task(index - 1)

        elif choice == "5":
            print("Good Bye 👋")
            break

        else:
            print("Invalid Option!")


if __name__ == "__main__":
    main()