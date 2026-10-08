from datetime import date

year = int(input("Birth year: "))

current_year = date.today().year
age = current_year - year

print("Age:", age)