students = {}

while True:
    name = input("Student name (exit): ")

    if name == "exit":
        break

    grade = float(input("Grade: "))
    students[name] = grade

print("\nResults:")

for name, grade in students.items():
    print(name, ":", grade)