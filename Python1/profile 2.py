def myfunction(**kwargs):
    for key , value in kwargs.items():
        print(key,value)
myfunction(name='arya')       
myfunction(name='ghavami',family='kazazi')
myfunction(name='arash',family='solamoni',city='tehran')