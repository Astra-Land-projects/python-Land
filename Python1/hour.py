hour =int(input("Enter hour into?"))

if (6 <= hour <= 10) or (16 <= hour <= 20):
    message = "Entry is allowed!"
else:
    message = "Entry is not allowed!" 

print(message)       