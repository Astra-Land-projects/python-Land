import json
from pathlib import Path

FILE = Path("expenses.json")

def load():
    if FILE.exists():
        return json.loads(FILE.read_text())
    return []

def save(data):
    FILE.write_text(json.dumps(data, indent=2))

expenses = load()

while True:
    print("\n1. Add expense")
    print("2. Show expenses")
    print("3. Total")
    print("4. Exit")

    choice = input("> ")

    if choice == "1":
        title = input("Title: ")
        amount = float(input("Amount: "))

        expenses.append({
            "title": title,
            "amount": amount
        })

        save(expenses)

    elif choice == "2":
        for e in expenses:
            print(f"{e['title']}: ${e['amount']:.2f}")

    elif choice == "3":
        print("Total:", sum(e["amount"] for e in expenses))

    elif choice == "4":
        break