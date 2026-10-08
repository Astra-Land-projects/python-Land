def square(x):
  return x ** 2

data = input("چند عدد وارد کن (با فاصله): ")
numbers = list(map(int, data.split()))
result = list(map(square, numbers))

for r in result:
  print(r, end=" ")