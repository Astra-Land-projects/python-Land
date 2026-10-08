import json
import os


class TaskManager:

    def __init__(self):
        self.file = "tasks.json"

        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title):
        self.tasks.append({
            "title": title,
            "done": False
        })
        self.save()
        print("Task Added.")

    def show_tasks(self):
        if not self.tasks:
            print("No Tasks.")
            return

        for i, task in enumerate(self.tasks, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {status} {task['title']}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            self.save()
            print("Completed.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save()
            print("Deleted.")