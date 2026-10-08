employees = []

while True:
    name = input("Employee name (exit): ")

    if name == "exit":
        break

    salary = float(input("Salary: "))

    employees.append({
        "name": name,
        "salary": salary
    })

for employee in employees:
    print(employee)