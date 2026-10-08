class BankAccount:
  # ویژگی کلاس
  count = 0

  # سازنده
  def __init__(self, name, account_number, balance):
    self.name = name
    self.account_number = account_number
    self.balance = balance

    # افزایش شمارنده هنگام ساخت حساب جدید
    BankAccount.count += 1

  # نمایش اطلاعات
  def __str__(self):
    return "نام: " + self.name + " | شماره حساب: " + self.account_number + " | موجودی: " + str(self.balance)

  # واریز به حساب
  def deposit(self, amount):
    self.balance += amount
    print("موجودی بعد از واریز:", self.balance)

  # برداشت از حساب
  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
      print("موجودی بعد از برداشت:", self.balance)
    else:
      print("!موجودی کافی نیست")


# ساخت حساب
acc1 = BankAccount("Ali", "12345", 5000)
acc2 = BankAccount("Sara", "67890", 8200)

# نمایش حساب
print(acc1)
print(acc2)