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
    def addback(self,x):
        t=self.head
        while (t.nxt!= None):
            t=t.nxt
        t.nxt = node(x)
    def addfront(self,x):
        t=self.head
        n_node=node(x)
        n_node.nxt=self.head
        self.head=n_node
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s+=t.data
                t=t.nxt
        print(s)
    
    def search(self,x):
        t=self.head
        while(t!=None):
            if (t.data==x):
                return "found"
            t=t.nxt
        return "not found"
    def addmiddle_evenod(self):
        F=self.head
        S=self.head
        while(F != None and F.nxt !=None):
            S=S.nxt
            F=F.nxt.nxt
        print(S.data)
    def length(self):
        F=self.head
        S=self.head
        while(F != None and F.nxt !=None):
            S=S.nxt
            F=F.nxt.nxt
        if (F==None):
            print("even")
        else:
            print("odd")
l1=sll() 
l2=sll() 
l1.head = node(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.addback(60)
l1.addback(70)
l1.addfront(1)
l1.addfront(2)
l1.display()
print()
l1.addeven()
print(l1.search(30))
print(l1.addmiddle_evenod())
print(l1.length())
l1.display()

