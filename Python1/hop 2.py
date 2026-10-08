number = 1 

while number <= 100:
    if number % 5 == 0:
        number += 1
        continue

    print(number)
    number += 1