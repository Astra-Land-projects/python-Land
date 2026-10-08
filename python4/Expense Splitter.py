# project_184_expense_splitter.py

people = int(input("People: "))
total = float(input("Total expense: "))

share = total / people

print(f"Each person pays: {share:.2f}")