def calculate(a, b, operator):
  try:
    # بررسی عملگر
    if operator == "+":
      print(a + b)
    elif operator == "-":
      print(a - b)
    elif operator == "*":
      print(a * b)
    elif operator == "/":
      print(a / b)
    else:
      print("!عملگر نامعتبر است")

  # مدیریت خطاهای مختلف
  except TypeError:
    print(".ورودی نامعتبر! فقط از اعداد صحیح و عملگرهای + - * / استفاده کنید")
  except ZeroDivisionError:
    print("!تقسیم بر صفر مجاز نیست")


calculate("2", "5", "*")
calculate("7", "+", "8")
calculate(20, 5, "/")
calculate(20, 0, "/")