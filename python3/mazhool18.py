class BankAccount:
  # سازنده
  def __init__(self, name, account_number, balance):
    self.name = name
    self.account_number = account_number
    self.balance = balance

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


# ساخت شیء به کمک سازنده
acc1 = BankAccount("Ali", "12345", 5000)
acc2 = BankAccount("Sara", "67890", 8200)

# نمایش اطلاعات حساب
acc1.show_info()
acc2.show_info()