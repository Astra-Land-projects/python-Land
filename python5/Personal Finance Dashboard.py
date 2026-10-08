import json

data = {
    "income": [],
    "expenses": []
}

def add_income():
    amount = float(input("Income: "))
    data["income"].append(amount)

def add_expense():
    amount = float(input("Expense: "))
    data["expenses"].append(amount)

def dashboard():
    income = sum(data["income"])
    expenses = sum(data["expenses"])
    balance = income - expenses

    print("\n===== FINANCE =====")
    print("Income:", income)
    print("Expenses:", expenses)
    print("Balance:", balance)

while True:
    print("\n1 Income")
    print("2 Expense")
    print("3 Dashboard")
    print("4 Exit")

    choice = input("> ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        dashboard()
    elif choice == "4":
        break