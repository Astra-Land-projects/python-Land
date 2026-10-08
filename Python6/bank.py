import json
import os


class Bank:

    def __init__(self):
        self.file = "accounts.json"

        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.accounts = json.load(f)
        else:
            self.accounts = []

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.accounts, f, indent=4)

    def create_account(self, name, balance):
        self.accounts.append({
            "name": name,
            "balance": balance
        })
        self.save()

    def show_accounts(self):
        for i, account in enumerate(self.accounts, start=1):
            print(f"{i}. {account['name']} | Balance: ${account['balance']}")

    def deposit(self, index, amount):
        if 0 <= index < len(self.accounts):
            self.accounts[index]["balance"] += amount
            self.save()

    def withdraw(self, index, amount):
        if 0 <= index < len(self.accounts):
            if self.accounts[index]["balance"] >= amount:
                self.accounts[index]["balance"] -= amount
                self.save()
            else:
                print("Insufficient Balance")

    def delete_account(self, index):
        if 0 <= index < len(self.accounts):
            self.accounts.pop(index)
            self.save()