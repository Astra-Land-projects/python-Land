class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def mohit(self):
        m=(self.width + self.height)*2
        return m
    def masahat(self):
        ma=self.width * self.height
        return ma
R1=rectangle(100,150)  
print("mohit=",R1.mohit())  
print("masahat=",R1.masahat())     