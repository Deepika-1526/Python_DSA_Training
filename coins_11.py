def fun(n):        
    l1=[0]*(n+1)
    i=l[0]
    l1[0]=1
    for j in range(1,n+1):
            if j==i:
                l1[j]=1
            else:
                l1[j]=0
    print(l1)
           
    
    for i in range(1,len(l)):
        l2=[0]*(n+1)
        print(l[i])
        l2[0]=1
        for j in range(1,n+1):
            if j<l[i]:
                l2[j]=l1[j]
            elif j==l[i]:
                l2[j]=1
            else:
                if l1[j]==1:
                    l2[j]=l1[j]
                else:
                    t=j-l[i]
                    te=l1[t]
                    l2[j]=te
        print(l2)
        l1=l2
    return l1[-1]
           

l=list(map(int,input().split()))
n=int(input())
t=fun(n)
if(t==1):
    print("yes")
else:
    print("no")