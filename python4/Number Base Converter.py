# project_191_base_converter.py

n = int(input("Number: "))
base = int(input("Base (2/8/16): "))

if base == 2:
    print(bin(n))
elif base == 8:
    print(oct(n))
elif base == 16:
    print(hex(n))
else:
    print("Unsupported base")
    