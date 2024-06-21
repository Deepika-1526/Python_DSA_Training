class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None
    def create(self,root,x):
        if (root==None):
            return node(x)
        elif (root.data>x):
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x)
        return root
             
            
    def inorder(self,root):
        if (root):
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
            
    def preorder(self,root):
        if (root):
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
             
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    
    def sumofnodes(self,root):
        if root==None:
            return 0
        return root.data+self.sumofnodes(root.left)+self.sumofnodes(root.right)
    
    def evennodes(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.evennodes(root.left)+self.evennodes(root.right)
        else:
            return self.evennodes(root.left) + self.evennodes(root.right)
    
    def oddnodes(self,root):
        if root==None:
            return 0
        if root.data%2!=0:
            return root.data+self.oddnodes(root.left)+self.oddnodes(root.right)
        else:
            return self.oddnodes(root.left) + self.oddnodes(root.right)
        
    
    def abssumnodes(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+ self.abssumnodes(root.left)+self.abssumnodes(root.right)
        return self.abssumnodes(root.left) + self.abssumnodes(root.right)-root.data
    
    def heightoftree(self,root):
        
        if root==None:
            return -1
        return max(self.heightoftree(root.left),self.heightoftree(root.right))+1
    
    def balance(self,root):
        
        if root==None:
            return 0
        return abs(self.heightoftree(root.left)-self.heightoftree(root.right))<=1
    
    def leafnodes(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.leafnodes(root.left)+self.leafnodes(root.right)
    
    def leafnodessum(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.data
        return self.leafnodessum(root.left)+self.leafnodessum(root.right)
    
    def search(self,root,x):
        if root==None:
            return 0
        if root.data==x:
            return 1
        if root.data>x:
            return self.search(root.left,x)
        else:
            return self.search(root.right,x)
        
    def depth(self,root,x,c):
        if root==None:
            return -1
        if root.data==x:
            return c
        if root.data>x:
            return self.depth(root.left,x,c+1)
        else:
            return self.depth(root.right,x,c+1)
    
    
    
t1=tree()
t1.root=node(10)
t1.create(t1.root,5)


t1.create(t1.root,20)
t1.create(t1.root,2)
t1.create(t1.root,7)
t1.create(t1.root,6)
t1.create(t1.root,8)
t1.create(t1.root,9)
'''t1.create(t1.root,25)
t1.create(t1.root,31)
t1.create(t1.root,50)'''


print("---INORDER TRAVERSAL-------")
t1.inorder(t1.root)
print()

print("---PRE-ORDER TRAVERSAL------")
t1.preorder(t1.root)
print()

print("---POST-ORDER TRAVERSAL------")
t1.postorder(t1.root)
print()

print("---SUM OF NODES--------------")
print("sum=",t1.sumofnodes(t1.root))

#print("left sub-tree-sum=",t1.sumofnodes(t1.root.left))#only left-sub tree sum
#print("absoultesum=",abs(t1.sumofnodes(t1.root.left)-t1.sumofnodes(t1.root.right)))
print("-----EVEN SUM---------------")
print("evensum:",t1.evennodes(t1.root))

print("-----ODD SUM----------------")
print("oddsum:",t1.oddnodes(t1.root))


print("------ABSOLUTE DIFFERENCE B/W EVEN NODES AND ODD NODES--------")
print(abs(t1.abssumnodes(t1.root)))

print("------HEIGHT OF THE TREE------")
print(t1.heightoftree(t1.root))

print("---TREE BALANCE OR NOT------")
if(t1.balance(t1.root)):
    print("balance")
else:
    print("Not balance")
    
    
print("------COUNT OF LEAF NODES------")
print(t1.leafnodes(t1.root))

print("------SUM OF LEAF NODES------")
print(t1.leafnodessum(t1.root))

print("------SEARCH FOR THE ELEMENT-------")
if(t1.search(t1.root,8)):
    print("found")
else:
    print("not found")
    
print("------DEPTH OF THE NODE-----")
print(t1.depth(t1.root,8,0))
    
    