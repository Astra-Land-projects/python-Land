total_pages = 0

with open("books.txt", "r") as file:
  # خواندن تمام خطوط
  books = file.readlines()

# پیمایش روی کتاب‌ها
for book in books:
  # پاکسازی و تقسیم اطلاعات به بخش‌های کوچک‌تر
  parts = book.strip().split(" - ")
  # دسترسی به تعداد صفحات
  pages = parts[-1]
  # تبدیل رشته به عدد و جمع با مقادیر قبلی
  total_pages += int(pages)

print("تعداد صفحات همه کتاب‌ها:", total_pages)