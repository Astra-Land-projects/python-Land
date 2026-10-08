import json
import os


class JSONDatabase:

    def __init__(self):
        self.file = "database.json"

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)

    def all(self):
        with open(self.file) as f:
            return json.load(f)

    def insert(self, item):
        data = self.all()

        data.append(item)

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)