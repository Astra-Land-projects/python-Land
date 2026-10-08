authors = ["John Smith", "Paulo Coelho", "Paulo Coelho", "John Steinbeck"]
books_count = [4, 1, 2, 3]

for i in range(len(authors)):
  # سعی کن دو مقدار رو به هم بچسبونی
  try:
    print(authors[i] + books_count[i])
  # اگر در عملیات به مشکل خوردی، کد زیر رو اجرا کن
  except TypeError:
    print(".نوع داده‌ها یکسان نیست")