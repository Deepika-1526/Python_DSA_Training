class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            self.tail.nxt=node(x)
            self.tail.nxt.prev=self.tail
            self.tail=self.tail.nxt
            
            '''we can write this too
            t=node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=self.tail.nxt'''
    
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            self.head.prev=node(x)
            self.head.prev.nxt=self.head
            self.head=self.head.prev
            
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="-->")
            t=t.nxt
        print()
        
    def bdisplay(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="<--")
            t=t.prev
        print()
        
    def search(self,x):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            if(t.data==x or t1.data==x):
                return "found"
            t=t.nxt
            t1=t1.prev
            
        if t.data==x:
            return 'found'
        return 'not found'
    
    
    def lengthevenodd(self):
        t=self.head
        t1=self.tail
        while(t!=t1):
            if(t1.nxt==t):
                return 'even'
            t=t.nxt
            t1=t1.prev
        return 'odd'
    
    def palin(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            if(t.data!=t1.data):
                return 'not palindrome'   
            t=t.nxt
            t1=t1.prev
        return 'palindrome'
    
    def manipulate(self):
        '''t=self.head
        t1=self.tail
        while(t!=t1.nxt):
            t=t.nxt
            t1=t1.prev
            
        t2=self.tail
        while(t1!=None):
            t2.data,t1.data=t1.data,t2.data
            t1=t1.prev
            t2=t2.prev'''
            
        f=self.head
        s=self.head
        while(f!=None):
            f=f.nxt.nxt
            s=s.nxt
        self.tail.nxt=self.head
        self.head.prev=self.tail
        t1=s.prev
        t1.nxt=None
        s.prev=None
        self.head=s
        self.tail=t1
        
                    
l1=dll()        

#l1.head=node(5)
#l1.tail=l1.head
'''l1.addfront(1)
l1.addfront(2)
l1.addfront(3)
l1.addfront(4)
l1.addfront(1)
#l1.addfront(1)
#l1.addfront(67)'''


l1.addback(3)
l1.addback(5)
l1.addback(7)
l1.addback(8)
l1.addback(9)
l1.addback(10)
l1.addback(12)
l1.addback(15)

l1.display()
l1.bdisplay()
print(l1.search(40))
print(l1.lengthevenodd())
print(l1.palin())
l1.manipulate()
l1.display()


