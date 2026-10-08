with open("books.txt", "r") as file:
  # خواندن تمام خطوط
  books = file.readlines()

# پیمایش روی کتاب‌ها
for book in books:
  # پاکسازی و تقسیم اطلاعات به بخش‌های کوچک‌تر
  parts = book.strip().split(" - ")
  title = parts[0]
  author = parts[1]
  genre = parts[2]
  pages = parts[3]
  # f-string چاپ اطلاعات به کمک
  print(f"نویسنده: {author} کتاب: {title}")