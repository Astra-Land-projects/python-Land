items = ["laptop" ,"mouse" ,"keyboard" ,"monitor" , "printer"]
price = [100 ,31 ,35 ,45 , 38]

for i in range(len(items)):
    if items[i] == "printer" or items[i] == "mouse":
        if price[i] - 10 < 30:
            price[i] = 30
        else:
            price[i] -= 10 
            
for i in range(len(items)):
    print(items[i] , price[i])               