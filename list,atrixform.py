'''
ip:[3,2,4,1,3,6,7,2]
op:
   3 2 4 1
   1 6 7 2
   convert data into matrix form
   
ip:[2,3,1,3,4,3,2]
 op:[[2 3 1 4],[1 2 3],[1 2]]
 
 ip:[4,5,2,1]
 op:[[4,5,2,1]]
   '''

l=list(map(int,input().split()))
'''l1=[]
c=0
while(c!=len(l)):
    r=[]
    for i in range(len(l)):
        if(not str(l[i]).isalpha()):
            if(l[i] not in r):
                c=c+1
                r.append(l[i])
                l[i]='a'
    l1.append(r)

print(l1)'''

d={}
m=[]
c=0
for i in l:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
while(c!=len(l)):
    r=[]
    for i in d:
        if(d[i]!=0):
            d[i]=d[i]-1
            c=c+1
            r.append(i)
    m.append(r)
print(m)

