class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t =self.head
        while(t != None):
            print(t.data,end="->")
            t = t.nxt
        print()
    def addback(self,x):
        t=self.head
        while (t.nxt!= None):
            t=t.nxt
        t.nxt = node(x)
    def check(self):
        m=0
        c=0
        t=self.head
        while(t.nxt!=None):
            if(t.nxt.data-t.data !=1):
                c+=1
                t=t.nxt
            else:
                if c>m:
                    m=c
                c=1
        if c>m:
            m=c
        return m
    '''def allpairs(self):
        t=self.head
        while(t.nxt!=None):
            t1=t.nxt
            while(t1!= None):
                print(t.data,t1.data)
                t1=t1.nxt
            t=t.nxt '''  
l1=sll() 
l2=sll() 
l1.head = node(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.addback(60)
l1.addback(70)
l2.head=node(100)
l2.addback(200)
l2.addback(300)
l1.display()
print()
l2.display()
#l1.allpairs()
l1.check()
l1.display()