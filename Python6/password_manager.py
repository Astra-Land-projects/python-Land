import json
import os


class PasswordManager:

    def __init__(self):
        self.file = "passwords.json"

        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.passwords = json.load(f)
        else:
            self.passwords = []

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.passwords, f, indent=4)

    def add_password(self, website, username, password):
        self.passwords.append({
            "website": website,
            "username": username,
            "password": password
        })
        self.save()

    def show_passwords(self):
        for i, item in enumerate(self.passwords, start=1):
            print(f"{i}. {item['website']} | {item['username']} | {item['password']}")

    def delete_password(self, index):
        if 0 <= index < len(self.passwords):
            self.passwords.pop(index)
            self.save()