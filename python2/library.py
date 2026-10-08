class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"subject: {self.title}\nwriter: {self.author}\nISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"book '{book.title}' to library plus!.")

    def search_book(self, query):
        results = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query.lower() in book.isbn:
                results.append(book)

        if results:
            print("result search:")
            for book in results:
                print(book)
                print("-" * 20)
        else:
            print("do not find any book with this info.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"book with ISBN '{isbn}' from library delete.")
                return
        print("book with this ISBN not find.")

    def display_books(self):
        if self.books:
            print("books list:")
            for book in self.books:
                print(book)
                print("-" * 20)
        else:
            print("your library is empety.")

# مثال استفاده
library = Library()

book1 = Book("HARRY POTTER, STRANG ROCK", "G.K.ROLING", "978-0747532743")
book2 = Book("100 HUNDERED ALONE", "GABRIAL MARISA MARKES", "978-0060883238")

library.add_book(book1)
library.add_book(book2)

library.search_book("HARRY")
library.display_books()
library.remove_book("978-0060883238")
library.display_books()