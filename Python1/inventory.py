inventory = {
    "apple":5,
    "banana":0,
    "orange":3,
    "watermelon":0,
    "graps":7
}
requested_items = ["banana","graps","kiwi","watermelon","apple","pinapple"]

for item in requested_items:
    if item in inventory and inventory[item] > 0:
        print(item,"it is")
        inventory[item] -= 1
    else:
        print(item,"it is not")    