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
    def bubblesort(self):
        c=0
        T=self.head
        p=None
        while(T.nxt!=None):
            f=0
            t=self.head
            while(t.nxt!=p):
                if(t.data>t.nxt.data):
                    f=1
                    t.data, t.nxt.data = t.nxt.data, t.data
                t=t.nxt
            if(f==0):
                break
            p=t
            T=T.nxt
        return c
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
l1.addback(7)
l1.addback(9)
l1.addback(4)
l1.addback(59)
l1.addback(66)
l1.addback(705)
l2.head=node(100)
l2.addback(200)
l2.addback(300)
l1.display()
print()
l2.display()
#l1.allpairs()
#l1.check()
#l1.display()
b=l1.bubblesort()
l1.display()
print(b)