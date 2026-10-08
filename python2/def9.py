def discount(price, percent=10):
  new_price = price * (1 - percent / 100)
  print(new_price)
discount(200000)
discount(200000, 20)
