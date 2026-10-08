def maximum(x,y,z):
    max=x
    if y > max:
        max=y
    if z > max:
        z=max
    return max
print('max',maximum(10,20,15))        