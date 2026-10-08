class BankAccount:
  name = ""
  account_number = ""
  balance = 0

  # نمایش اطلاعات
  def show_info(self):
    print("نام:", self.name)
    print("شماره حساب:", self.account_number)
    print("موجودی:", self.balance)

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


# ساخت شیء
acc1 = BankAccount()
acc1.name = "علی"
acc1.account_number = "12345"
acc1.balance = 5000

# واریز
acc1.deposit(1000)
# برداشت با موجودی کافی
acc1.withdraw(1000)
# برداشت با موجودی ناکافی
acc1.withdraw(10000)