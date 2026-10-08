import random
secret_number = random(1,100)
print("یک عدد بین 1 تا 100 انتخاب کن")

while True:
    guess = int(input("حدس :"))

    if guess < secret_number:
        print("عدد من بزرگ تره")
        
    elif guess > secret_number:
        print("عدد من کوچیک تره")

    else:
        print("افرین درست حدس زدی")
        break

