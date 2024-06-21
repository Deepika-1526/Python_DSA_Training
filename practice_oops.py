class qwer:
    def __init__(self,u,v):
        self.a=u
        self.b=v
    def fun(self,x):
        print("hello")
class asd(qwer):
    def fun(self):
        print("hi",self.a)
x = qwer(40,10)
y=asd(80,10)
y.fun(20)