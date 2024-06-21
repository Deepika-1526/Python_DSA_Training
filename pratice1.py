class A:
    def fun(self):
        print("hi") 
class B:
    def fun(self):
        print("hey")
class C(B,A):
    def fun1(self):
        print("hello")
x=C()
x.fun()