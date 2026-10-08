with open("books.txt", "r") as file:
  # خواندن تمام خطوط
  books = file.readlines()

# پیمایش روی کتاب‌ها
for book in books:
  # پاکسازی و تقسیم اطلاعات به بخش‌های کوچک‌تر
  parts = book.strip().split(" - ")
  print("عنوان:", parts[0])
  print("نویسنده:", parts[1])
  print("ژانر:", parts[2])
  print("صفحات:", parts[3])
  print("-----")