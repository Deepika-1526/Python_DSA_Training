'''def fun(graph,n):
    q=[n]
    while(q):
        for i in graph[q[0]]:
            if i not in q and i not in vi:
                q.append(i)
        vi.append(q.pop(0))
        print(vi[-1],end=" ")   
#graph={5:[7,3],7:[5,4,3],4:[7,8,2],3:[5,7,8],8:[3,4,2],2:[4,8]}
graph={1:[2,3,7],2:[5,10,4],3:[6,7],4:[2,10,9],5:[2],6:[3],7:[8,3],8:[7],9:[4],10:[4,2,11],11:[10]}
v=next(iter(graph))
vi=[]
q=[]
fun(graph,v)'''
def fun(d,x):
    v=[]
    q=[x]
    while(q):
        for i in d[q[0]]:
            if i not in v and i not in q:
                q.append(i)
        v.append(q.pop(0))
        return v
    
    
#d={5:[7,3],7:[5,4,3],4:[7,8,2],3:[5,7,8],8:[3,4,2],2:[4,8]}
d={1:[2,3,7],2:[5,10,4],3:[6,7],4:[2,10,9],5:[2],6:[3],7:[8,3],8:[7],9:[4],10:[4,2,11],11:[10]}
print(fun(d,next(iter(d))))