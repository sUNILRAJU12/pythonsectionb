class A:
    a=10
    b=20

    def __init__(self,c,d):
        self.c=c
        self.d=d

class C(B):
    b=40

    def __init__(self,c,d,e,f):
        super().__init__(c,d)
        self.e = e
        self.f = f
class C(D):
    D=50

    def display(self):
        #parent.display(self)
        super().display()
        print(self.e,self.f)
obj = C(4,5,6,7) 