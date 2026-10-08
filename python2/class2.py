class Item:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

# اضافه کردن کالا
item1 = Item("Laptop", 40000000, 10)
item2 = Item("Mouse", 2000000, 18)
item3 = Item("Keyboard", 5000000, 15)

# چاپ اسامی کالاها
print(item1.name)
print(item2.name)
print(item3.name)