try:
  with open("boooks.txt", "r") as file:
    line1 = file.readline()
    print(line1)
# اگر فایل وجود نداشت، کد زیر رو اجرا کن
except FileNotFoundError:
  print(".فایل پیدا نشد")