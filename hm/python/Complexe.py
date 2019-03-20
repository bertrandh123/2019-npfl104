class Complexe:
    def __init__(self,re,im):
      self.re,self.im=re,im
    
    def add(self,r,i):
      self.re+=r
      self.im+=i
    
    def sub(self,r,i):
      self.re+=-r
      self.im+=-i

    def __str__(self):
      if self.im>0:
        print(str(self.re)+'+'+str(self.im)+'i')
      else:
        print(str(self.re)+str(self.im)+'i')

print ("\n########## Class Complexe ##########\n")
C=Complexe(4,-2)
print('C=Complexe(4,-2)')
print("C.__str__()")
print(C.__str__())
C.add(1,6)
print('C.add(1,6)')
print("C.__str__()")
print(C.__str__())
print ("\n######## End Class Complexe ########\n")