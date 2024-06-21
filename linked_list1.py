class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def display(self):
        t = head
        while(t != None):
            print(t.data)
            t = t.nxt
    def addback(self,x):
        t=head
        while (t.nxt!= None):
            t=t.nxt
        t.nxt = node(x)
l1=sll()  
head = node(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.addback(60)
l1.addback(70)
l1.display()