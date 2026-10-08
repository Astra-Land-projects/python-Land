class Book:
  def __init__(self, title, isbn):
    self.isbn = isbn
    self.title = title
    self.is_borrowed = False

class Borrow:
  def __init__(self, user_id, book):
    if book.is_borrowed:
      print("کتاب در دسترس نیست")
      return

    self.user_id = user_id
    self.book = book
    book.is_borrowed = True

# ایجاد کتاب جدید
lotr = Book("Lord Of The Rings", "9780544003415")
# وضعیت امانت قبل از قرض کتاب
print(lotr.is_borrowed)

# ثبت اطلاعات برای قرض کتاب بالا
new_borrow = Borrow("1", lotr)
#  وضعیت امانت بعد از قرض کتاب
print(lotr.is_borrowed)