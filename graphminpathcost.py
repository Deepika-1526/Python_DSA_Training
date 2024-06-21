#mimimum path
def fun(d,x,e,c,m,l1):
    l.append(x)
    if x==e:
        if c<m:
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
            
    for i in d[x]:
        if(i[0] not in l):
            m,l1=fun(d,i[0],e,c+i[1],m,l1)
    l.pop()
    return m,l1   
d={5:[(7,1),(3,3)],7:[(5,1),(4,3),(3,2)],4:[(7,3),(8,6),(2,3)],8:[(3,5),(4,6),(2,2)],3:[(5,3),(7,2),(8,5)],2:[(4,3),(8,2)]}


l=[]
print(fun(d,5,2,0,99999,[])) 















