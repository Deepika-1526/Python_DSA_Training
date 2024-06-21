def fun(d,x,e,c):
    l.append(x)
    if x==e:
        print(l,c)
        l.pop()
        return c
    for i in d[x]:
        #print(i,j)
        if(i[0] not in l):
            fun(d,i[0],e,c=c+i[1])
    l.pop()
    
d={5:[(7,1),(3,3)],7:[(5,1),(4,3),(3,2)],4:[(7,3),(8,6),(2,3)],8:[(3,5),(4,6),(2,2)],3:[(5,3),(7,2),(8,5)],2:[(4,3),(8,2)]}


l=[]
fun(d,5,2,0)
