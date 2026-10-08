import datetime as dt
import pandas as pd


# تابع برای افزودن خرج
def add_expense(category, amount, notes):
  df = pd.read_csv("expenses.csv")
 
  new_row = pd.DataFrame([{
    "date": dt.date.today(),
    "category": category,
    "amount": amount,
    "notes": notes
  }])

  df = pd.concat([df, new_row], ignore_index=True)
  df.to_csv("expenses.csv")


# تابع برای مشاهده آخرین خرج
def recent_expense():
  df = pd.read_csv("expenses.csv")
  result = df.tail(1)

  if result.shape[0] == 0:
    return "خرجی وجود ندارد"
  else:
    return f"""
    تاریخ: {df.tail(1)["date"].values[0]}
    دسته‌بندی: {df.tail(1)["category"].values[0]}
    مقدار خرج: {df.tail(1)["amount"].values[0]}
    توضیحات: {df.tail(1)["notes"].values[0]}
    """


# تابع برای مشاهده تمام خرج‌ها
def total_expenses():
  # خواندن فایل داده‌ها
  df = pd.read_csv("expenses.csv")

  if df.shape[0] == 0:
    return "خرجی وجود ندارد"
  else:
    category_sum = df.groupby('category')['amount'].sum()
    message = ""
    for cat, total in category_sum.items():
      message += f"{cat}: {total}\n"

    sum = df['amount'].sum()
    message += f"مجموع: {sum}"
    return message


# منوی اصلی
menu = """
----------
1. افزودن خرج
2. مشاهده آخرین خرج
3. مشاهده تمام خرج‌ها
4. خروج
"""

message = "مدیریت خرج‌ها"


while True:
  # نمایش منوی اصلی و دریافت انتخاب کاربر
  user_input = input(message + menu).strip()

  # افزودن خرج
  if user_input == "1":
    category = input("دسته‌بندی").strip()

    amount = float(input("مقدار خرج"))
    while amount < 0:
      amount = float(input("مقدار خرج"))

    notes = input("توضیحات")
   
    add_expense(category, amount, notes)
    message = f"خرج جدید در دسته «{category}» اضافه شد"

  #  مشاهده آخرین خرج
  elif user_input == "2":
    message = recent_expense()

  # مشاهده تمام خرج‌ها
  elif user_input == "3":
    message = total_expenses()

  # خروج از برنامه
  elif user_input == "4":
    break