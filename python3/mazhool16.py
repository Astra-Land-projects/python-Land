# تعریف کلاس
class BankAccount:
  name = ""
  account_number = ""
  balance = 0

# ساخت شیء
acc1 = BankAccount()

# تغییر مقدار ویژگی‌ها
acc1.name = "Ali"
acc1.account_number = "12345"
acc1.balance = 5000

# چاپ ویژگی‌ها
print("نام:", acc1.name)
print("شماره حساب:", acc1.account_number)
print("موجودی:", acc1.balance)