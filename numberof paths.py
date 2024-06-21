#count of paths of graph
def dfs(d,x,e,c):
    l.append(x)
    if x==e:
        c+=1
        l.pop()
        return c
    for i in d[x]:
        if(i not in l):
            c=dfs(d,i,e,c)
    l.pop()
    return c
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
print(dfs(d,5,2,0))