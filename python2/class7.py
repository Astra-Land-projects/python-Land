import datetime

class Customer:
  # سازنده
  def __init__(self, name, email, address):
    self.name = name
    self.email = email
    self.address = address
    self.is_verified = False

  # نمایش اطلاعات
  def show_info(self):
    print("- مشتری -")
    print(self.name, "(", self.email, ")")
    if self.is_verified:
      print(".حساب تایید شده است")
    else:
      print(".حساب تایید نشده است")

  # تایید حساب
  def verify(self):
    if not self.is_verified:
      self.is_verified = True
      print(".حساب شما تایید شد")


# مشتری جدید
customer1 = Customer("Ali", "Ali@gmail.com", "Tehran-Jordan")

# تایید حساب مشتری
customer1.verify()

# نمایش اطلاعات مشتری
customer1.show_info()