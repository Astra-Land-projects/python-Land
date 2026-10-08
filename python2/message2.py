message1="python programming Book"
print(message1.find("o"))
print(message1.find("o",7,18))
print(message1.find("z"))
print(message1.rfind("o"))
print(message1.rfind("o",0,18))
print(message1.rfind("z"))
print(message1.index("p"))
print(message1.index("o",7,18))
#print(message1.index("p")) error
print(message1.rindex("p"))
print(message1.rindex("o",19,23))
#print(message1.rindex("p")) error
print(message1.startswith("Py"))
print(message1.startswith("My"))
print(message1.startswith("Pro",7,18))
print(message1.endswith("ok"))
print(message1.endswith("os"))
print(message1.endswith("ing",7,18))
