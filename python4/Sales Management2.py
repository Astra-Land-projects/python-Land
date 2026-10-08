import json
import os


class SalesManager:

    def __init__(self):
        self.file = "sales.json"

        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.products = json.load(f)
        else:
            self.products = []

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.products, f, indent=4)

    def add_product(self, name, price, quantity):
        self.products.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
        self.save()

    def show_products(self):
        if not self.products:
            print("No Products.")
            return

        for i, p in enumerate(self.products, start=1):
            print(f"{i}. {p['name']} | ${p['price']} | Stock: {p['quantity']}")

    def sell_product(self, index, qty):
        if 0 <= index < len(self.products):
            if self.products[index]["quantity"] >= qty:
                self.products[index]["quantity"] -= qty
                self.save()
                print("Sale Successful")
            else:
                print("Not Enough Stock")

    def delete_product(self, index):
        if 0 <= index < len(self.products):
            self.products.pop(index)
            self.save()