weight = float(input("Enter your weight?"))
age = int(input("Enter your age?"))

ticket = 0 

if weight < 70 or age < 12:
    print("sorry you can not play.")
else:
    if 12 <= age <= 18:
        ticket += 100000
    else:
        ticket += 150000

    picture = input("do want take a image when you play?")
    if picture == "yes":
      ticket += 30000

print("price your ticket", "->", ticket)                  