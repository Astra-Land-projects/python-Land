import json
import os


class InventoryManager:

    def __init__(self):
        self.file = "inventory.json"

        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.items = json.load(f)
        else:
            self.items = []

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.items, f, indent=4)

    def add_item(self, name, quantity):
        self.items.append({
            "name": name,
            "quantity": quantity
        })
        self.save()
        print("Item Added.")

    def show_items(self):
        if not self.items:
            print("Inventory Empty.")
            return

        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item['name']} | Qty: {item['quantity']}")

    def update_quantity(self, index, quantity):
        if 0 <= index < len(self.items):
            self.items[index]["quantity"] = quantity
            self.save()
            print("Quantity Updated.")

    def delete_item(self, index):
        if 0 <= index < len(self.items):
            self.items.pop(index)
            self.save()
            print("Item Deleted.")