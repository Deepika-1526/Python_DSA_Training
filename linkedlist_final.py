class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def _init_(self):
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
        t=node(x)
        t.nxt=self.head
        self.head=t

    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s+=t.data
                t=t.nxt
        print(s)
    def addmiddle_evenod(self):
        F=self.head
        S=self.head
        while(F != None and F.nxt !=None):
            S=S.nxt
            F=F.nxt.nxt
        print(S.data)
    '''def length(self):
        F=self.head
        S=self.head
        while(F != None and F.nxt !=None):
            S=S.nxt
            F=F.nxt.nxt
        if (F==None):
            print("even")
        else:
            print("odd")'''
    '''def search(self,x):
        t=self.head
        while(t!=None):
            if (t.data==x):
                return "found"
            t=t.nxt
        return "not found"
    #def longeststr(self):

    def allpairs(self):
        t=self.head
        while(t.nxt!=None):
            t1=t.nxt
            while(t1!= None):
                print(t.dat,t1.data)
                t1-t1.nxt
            t=t.nxt'''

l1=sll() 
l1.head = node(10)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.addback(60)
l1.addback(70)
l1.display()
print()
print()
l1.addeven()
print(l1.addmiddle_evenod())
#print(l1.length())
#print(l2.search(100))
#l1.allpairs()
