import json
import os


class StudentManager:

    def __init__(self):
        self.file = "students.json"

        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.students = json.load(f)
        else:
            self.students = []

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.students, f, indent=4)

    def add_student(self, name, age, grade):
        self.students.append({
            "name": name,
            "age": age,
            "grade": grade
        })
        self.save()
        print("Student Added.")

    def show_students(self):
        if not self.students:
            print("No Students.")
            return

        for i, student in enumerate(self.students, start=1):
            print(f"{i}. {student['name']} | Age: {student['age']} | Grade: {student['grade']}")

    def update_grade(self, index, grade):
        if 0 <= index < len(self.students):
            self.students[index]["grade"] = grade
            self.save()
            print("Grade Updated.")

    def delete_student(self, index):
        if 0 <= index < len(self.students):
            self.students.pop(index)
            self.save()
            print("Student Deleted.")