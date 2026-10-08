colors1=["red","green","blue"]
print(colors1)

colors1.append("yellow")
print(colors1)

colors1.insert(1,"cyan")
print(colors1)

colors2=["black","white","gray"]
colors1.extend(colors2)
print(colors1)

colors1.pop()
print(colors1)
colors1.pop(2)
print(colors1)
#colors1.pop(7) error

colors1.remove("blue")
print(colors1)
#colors1.remove("orange") error

colors1.clear()
print(colors1)
