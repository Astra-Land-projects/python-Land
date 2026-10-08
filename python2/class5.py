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
    # اعتبارسنجی
    if item.quantity > 0:
      self.customer = customer
      self.item = item
      self.order_date = datetime.date.today()
      item.quantity -= 1 # کم کردن موجودی
      print(".یک سفارش جدید ثبت شد")
    else:
      print("!سفارش ناموفق - موجودی کالا کافی نیست")

# اضافه کردن کالا
item1 = Item("Laptop", 40000000, 10)
item2 = Item("Mouse", 2000000, 18)
item3 = Item("Keyboard", 5000000, 15)
item4 = Item("VR Headset", 32000000, 2)

# ثبت سفارش
new_order1 = Order("Sara", item4)
new_order2 = Order("Reza", item4)
new_order3 = Order("Shadi", item4)