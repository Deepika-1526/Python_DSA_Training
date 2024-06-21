def fun(d,l,n,x):         #n = strat node , x = end node
    l.append(n)
    if n==x:
        print(l)
        l.pop()
        return 
    for i in d[n]:
        if i not in l:
            fun(d,l,i,x)
    l.pop()
d={5:[(7),(3)],7:[(5),(4),(3)],4:[(7),(8),(2)],8:[(4),(3),(2)],3:[(5),(7),(8)],2:[(4),(8)]}
for i in d.keys():
    print("5"+"----> ",end="")
    print(i)
    fun(d,[],5,i)