class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def create(self, root, x):
        if root is None:
            return Node(x)
        elif x < root.data:
            root.left = self.create(root.left, x)
        else:
            root.right = self.create(root.right, x)
        return root

    def insert(self, x):
        self.root = self.create(self.root, x)

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

# sum of all the elements
    def sum(self, root):
        if root is None:
            return 0
        else:
            return root.data + self.sum(root.left) + self.sum(root.right)
        
#sum of left subtree        
    def sum_left_subtree(self, root):
        if root is None:
            return 0
        elif root.left:
            return root.data + self.sum_left_subtree(root.left) + self.sum_left_subtree(root.right)
        else:
            return root.data
        
# sum of even and odd elements 
    def sum_even_odd(self, root):
        if root is None:
            return 0, 0
        else:
            even_sum = 0
            odd_sum = 0
            if root.data % 2 == 0:
                even_sum += root.data
            else:
                odd_sum += root.data
            even_sum_left, odd_sum_left = self.sum_even_odd(root.left)
            even_sum_right, odd_sum_right = self.sum_even_odd(root.right)
            even_sum += even_sum_left + even_sum_right
            odd_sum += odd_sum_left + odd_sum_right
            return even_sum, odd_sum
    def print_even_odd_sum(self):
        even_sum, odd_sum = self.sum_even_odd(self.root)
        print(even_sum)
        print(odd_sum)


#absolute difference 
    def absolute_difference(self, root):
        even_sum, odd_sum = self.sum_even_odd(root)
        return abs(even_sum - odd_sum)
    
#height of a tree
    def height(self, root):
        if root== None:
            return -1
        return max (self.height(root.left), self.height(root.right)) + 1
    
#balanced tree
    def balanced_tree(self,root):
        if(root==None):
            return True
        if abs(self.height(root.left) - self.height(root.right)) <=1:
            return True
        return False
    
#count of leaf nodes
    def leafnodecnt(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.leafnodecnt(root.left)+self.leafnodecnt(root.right)
    

#sum of leaf nodes

    def sum_leaf_nodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        return self.sum_leaf_nodes(root.left) + self.sum_leaf_nodes(root.right)
    
#search of the element

    def search(self,root,key):
        if (root== None) or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        return self.search(root.right, key)
        result = self.search(self.root, key)
    def search_element(self,key):
        result = self.search(self.root, key)
        if result:
            print(f"Element {key} is found in the tree.")
        else:
            print(f"Element {key} is not found in the tree.")

#depth of the element 
    def depth(self, root, y, c=0):
        if root is None:
            return -1
        if root.data == y:
            return c
        left_depth = self.depth(root.left, y, c + 1)
        right_depth = self.depth(root.right, y, c + 1)
        if left_depth!= -1:
            return left_depth
        else:
            return right_depth
        

#top view of the tree
    '''def topview(self,root,c,dict1):
        if root==None:
            return 
        if c not in dict1:
            print(root.data,end=" ")
            dict1.update({c:root.data})
        self.topview(root.left,c+1,dict1)  
        self.topview(root.right,c-1,dict1)'''
    def topview(self,root):
        if(root==None):
            return
        d={}
        q=[(root,0)]
        while(q):
            root = q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            if(q[0][1] not in d):
                d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")



#left view of the tree
    def leftview(self,root,c,l):
        if(root==None):
            return
        if(c not in l):
            l.append(c)
            print(root.data, end=' ')
        self.leftview(root.left,c+1,l)
        self.leftview(root.right,c+1,l)


#right view of the tree
    def rightview(self,root,c,l):
        if(root==None):
            return
        if(c not in l):
            l.append(c)
            print(root.data, end=' ')
        self.rightview(root.right,c+1,l)
        self.rightview(root.left,c+1,l)

#bottom view of tree
    def bottomview(self,root):
        if(root==None):
            return
        d={}
        q=[(root,0)]
        while(q):
            root = q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")

t1 = Tree()
t1.root=Node(10)
t1.insert(5)
t1.insert(15)
t1.insert(7)
t1.insert(11)
t1.insert(8)
t1.insert(9)
t1.insert(2)


total_sum = t1.sum(t1.root)
#total_sum = t1.sum(t1.root.left)
print(total_sum)
left_subtree_sum = t1.sum_left_subtree(t1.root.left)
print(left_subtree_sum)
t1.print_even_odd_sum()
absolute_diff = t1.absolute_difference(t1.root)
print(absolute_diff)
hei=t1.height(t1.root)
print(hei)
balancing_tree = t1.balanced_tree(t1.root)
if balancing_tree:
    print("True")
else:
    print("False")
print(t1.leafnodecnt(t1.root))
leaf_sum = t1.sum_leaf_nodes(t1.root)
print(leaf_sum)
search = 4
t1.search_element(search)
print(t1.depth(t1.root, 5))
print()
t1.topview(t1.root)
print()
t1.leftview(t1.root,0,[])
print()
t1.rightview(t1.root,0,[])
print()
t1.bottomview(t1.root)
print()
print("Preorder Traversal:")
t1.preorder(t1.root)  

print("\nInorder Traversal:")
t1.inorder(t1.root)

print("\nPostorder Traversal:")
t1.postorder(t1.root) 
