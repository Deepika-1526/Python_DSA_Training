def fun(root):
    if (root==None):
        return 
    print(root.data)
    fun(root.left)
    fun(root.right)
