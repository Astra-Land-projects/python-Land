import math
class circle:
   def __init__(self,r):
      self.r=r
   def masahat(self):
      ma=self.r**2*math.pi
      return ma
   def mohit(self):
      mo=self.r*2*math.pi
      return mo
c1=circle(10) 
print('masahat=',c1.masahat())  
print('mohit=',c1.mohit())  