import json
import os


class Library:

    def __init__(self):
        self.file = "books.json"

        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.books = json.load(f)
        else:
            self.books = []

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.books, f, indent=4)

    def add_book(self, title, author):
        self.books.append({
            "title": title,
            "author": author,
            "borrowed": False
        })
        self.save()

    def show_books(self):
        if not self.books:
            print("No Books.")
            return

        for i, book in enumerate(self.books, start=1):
            status = "Borrowed" if book["borrowed"] else "Available"
            print(f"{i}. {book['title']} - {book['author']} ({status})")

    def borrow_book(self, index):
        if 0 <= index < len(self.books):
            self.books[index]["borrowed"] = True
            self.save()

    def return_book(self, index):
        if 0 <= index < len(self.books):
            self.books[index]["borrowed"] = False
            self.save()

    def delete_book(self, index):
        if 0 <= index < len(self.books):
            self.books.pop(index)
            self.save()