import random

target = random.randint(1, 100)
while True:
    g = int(input("Guess 1-100: "))
    if g == target:
        print("Correct!")
        break
    print("Too low" if g < target else "Too high")