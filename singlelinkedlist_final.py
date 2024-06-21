'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
a=node(10)
b=node(20)
c=node(30)
d=node(40)


print(a.data,a.nxt)
print(b.data,b.nxt)

10 None
20 None
now we have link 2 nodes
'''

'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
a=node(10)
b=node(20)
c=node(30)
d=node(40)

a.nxt=b
b.nxt=c
c.nxt=d

print(a.data,a.nxt)
print(b.data,b.nxt)
print(c.data,c.nxt)
print(d.data,d.nxt)'''


'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
        
head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)


print(head.data)
print(head.nxt.data)
print(head.nxt.nxt.data)

o/p:
10
20
30

'''


'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
        
head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)

t=head
print(t.data)

assigning temp to the head node
'''


'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
        
head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)

t=head
while(t!=None):
    print(t.data)
    t=t.nxt
    
by this logic we can print how many nodes we want    
    '''


'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None

def display():
    t=head
    while(t!=None):
        print(t.data)
        t=t.nxt
    
        
head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)

display()'''


'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def display(self):
        t=head
        while(t!=None):
            print(t.data)
            t=t.nxt
    
l1=sll()        
head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)

l1.display()'''


'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def display(self):
        s=0
        t=head
        while(t!=None):
            s=s+t.data
            t=t.nxt
        print(s)
    
l1=sll()        
head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)

l1.display()'''


'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def display(self):
        t=head
        while(t!=None):
            print(t.data)
            t=t.nxt
    
l1=sll()        
head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)

t=head
while(t.nxt!=None):
    t=t.nxt
t.nxt=node(40)


l1.display()'''


'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def display(self):
        t=head
        while(t!=None):
            print(t.data)
            t=t.nxt
    def addback(self,x):
        t=head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    
l1=sll()        

head=node(9)
l1.addback(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)

l1.display()'''

'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="-->")
            t=t.nxt
        print()
        
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    
l1=sll()        
l2=sll()

l1.head =node(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)

l2.head =node(100)
l2.addback(200)
l2.addback(300)

l1.display()
l2.display()'''


class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="-->")
            t=t.nxt
        print()
        
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
        
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            t=t.nxt
        print(s)
    
    def addbeg(self,x):
        if self.head==None:
            t=node(x)
            self.node=t
        else:
            t=node(x)
            t.nxt=self.head
            self.head=t
            
    def search(self,x):
        t=self.head
        while(t!=None):
            if(t.data==x):
                return "found"
            t=t.nxt
        return "not found"
    
    def midnum(self):
        s=self.head
        f=self.head
        while(f!=None and f.nxt!=None):
                s=s.nxt
                f=f.nxt.nxt
        print(s.data)
    
    def length(self):
        f=self.head
        while(f!=None and f.nxt!=None):
                f=f.nxt.nxt
        if f==None:
            print("even")
        else:
            print("odd")
    
    def sequence(self):
        c,c1=1,1
        t=self.head
        while t.nxt!=None:
            if (t.nxt.data)-(t.data)==1:
                c=c+1
            else:
                c1=max(c,c1)
                c=1
            t=t.nxt
            
        if (c>c1):#print(max(c,c1)) 
            print(c)
        else:
            print(c1)
            
    
    def pairs(self):
        t=self.head
        while(t.nxt!=None):
            t1=t.nxt
            while(t1!=None):
                print(t.data,end="")
                print(t1.data,end=" ")
                t1=t1.nxt
            t=t.nxt
            print()

            
                
        
        
            
            
        
    
l1=sll()        
l2=sll()

l1.head=node(6)
l1.addback(7)
l1.addback(4)
l1.addback(8)
l1.addback(4)
l1.addback(2)
l1.addback(0)
l1.addback(1)


l2.head =node(100)
l2.addback(200)
l2.addback(300)

l1.display()
l2.display()

l1.addeven()
print(l1.search(50))

l1.midnum()
l1.length()
l1.sequence()
l1.pairs()


