temperature = int(input("Enter the weather degree?"))

if temperature < 10:
    message = "the weather is cold"
elif temperature > 25:
    message = "the weather is hot"
else:
    message = "the weather is good"

print(message)        