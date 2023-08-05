########### methord overriding ########### 
# we can override the methord using the super keyword
class S:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y
    
class C(S):
    def __init__(self,rad):
        self.rad = rad

    def area(self):
        return 3.14 * self.rad * self.rad


rec = S(3,5)
print(rec.area())
cir = C(5)
print(cir.area())
