import json
import os


class NotesApp:

    def __init__(self):
        self.file = "notes.json"

        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.notes = json.load(f)
        else:
            self.notes = []

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.notes, f, indent=4)

    def add_note(self, text):
        self.notes.append(text)
        self.save()
        print("Note Saved.")

    def show_notes(self):
        if not self.notes:
            print("No Notes.")
            return

        for i, note in enumerate(self.notes, start=1):
            print(f"{i}. {note}")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            self.notes.pop(index)
            self.save()
            print("Deleted.")