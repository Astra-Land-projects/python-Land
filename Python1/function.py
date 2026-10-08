def myfunction(*args):
    sum=0
    for arg in args:
        if arg % 2 == 0:
            sum=sum+arg
    return sum
print(myfunction(10))    
print(myfunction(10,15))    
print(myfunction(10,13,17))
print(myfunction(10,20,15,100))
print(myfunction(10,17,15,11,10))