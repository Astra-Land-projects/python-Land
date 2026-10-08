import datetime

# تعریف کلاس کالا
class Item:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

# تعریف کلاس سفارش
class Order:
  def __init__(self, customer, item):
    self.customer = customer
    self.item = item
    self.order_date = datetime.date.today()
    print(".یک سفارش جدید ثبت شد")

# اضافه کردن کالا
item1 = Item("Laptop", 40000000, 10)
item2 = Item("Mouse", 2000000, 18)
item3 = Item("Keyboard", 5000000, 15)

# ثبت سفارش
new_order = Order("Ali", item1)