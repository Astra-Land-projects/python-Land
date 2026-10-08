with open("books.txt", "r") as file:
  # خواندن تمام خطوط
  books = file.readlines()

# پیمایش روی کتاب‌ها
for book in books:
  # پاکسازی و تقسیم اطلاعات به بخش‌های کوچک‌تر
  parts = book.strip().split(" - ")
  title = parts[0]
  pages = parts[-1]

  # سعی کن تعداد صفحات رو به عدد صحیح تبدیل کنی
  try:
    if int(pages) < 200:
      print(f"{title} - {pages}")
  # اگر در تبدیل رشته به عدد به مشکل خوردی، کد زیر رو اجرا کن
  except ValueError:
    print("مشکل در خواندن کتاب")