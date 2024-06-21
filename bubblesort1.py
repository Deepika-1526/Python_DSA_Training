a=[3,2,6,8,10,9]
c=0
for i in range(len(a)-1):
    f=0
    for j in range(len(a)-1):
        if(a[j]>a[j+1]):
            f=1
            a[j],a[j+1],a[j+1],a[j]
        c=c+1
    if(f==0):
        break
print(a,c)