a=list(map(int,input().split()))
for i in range(len(a)-2):
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
    if(a[i+1]>a[i+2]):
        a[i+1],a[i+2]=a[i+2],a[i+1]
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
print(a)