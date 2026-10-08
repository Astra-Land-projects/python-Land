import json
import os


class EmployeeManager:

    def __init__(self):
        self.file = "employees.json"

        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.employees = json.load(f)
        else:
            self.employees = []

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.employees, f, indent=4)

    def add_employee(self, name, job, salary):
        self.employees.append({
            "name": name,
            "job": job,
            "salary": salary
        })
        self.save()

    def show_employees(self):
        for i, emp in enumerate(self.employees, start=1):
            print(f"{i}. {emp['name']} | {emp['job']} | ${emp['salary']}")

    def update_salary(self, index, salary):
        if 0 <= index < len(self.employees):
            self.employees[index]["salary"] = salary
            self.save()

    def delete_employee(self, index):
        if 0 <= index < len(self.employees):
            self.employees.pop(index)
            self.save()