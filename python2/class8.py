class Admin:
  # سازنده
  def __init__(self, name, email, permissions):
    self.name = name
    self.email = email
    self.permissions = permissions

  # نمایش اطلاعات
  def show_info(self):
    print("- ادمین -")
    print(self.name, "(", self.email, ")")
    print("دسترسی‌ها:", self.permissions)

  # اضافه کردن دسترسی
  def add_permission(self, new_permission):
    if new_permission not in self.permissions:
      self.permissions.append(new_permission)
      print(".دسترسی جدید اضافه شد")


# اضافه کردن ادمین جدید
admin1 = Admin("Arad", "Arad@gmail.com", ["add_item"])

# اضافه کردن دسترسی جدید به ادمین
admin1.add_permission("edit_item")

# نمایش اطلاعات ادمین
admin1.show_info()