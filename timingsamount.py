'''
ip:2 lists
[(1,3) (2,5) (4,6) (6,7) (5,8) (7,9)]--->timings
[5,6,5,4,11,2]--->momey
op:what is the largest amount you can get



'''
l1=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=a.copy()
for i in range(1,len(a)):
    for j in range(0,i):
        if(l1[j][1]<=l1[i][0]):
            if(b[j]+a[i]>b[i]):
                b[i]=b[j]+a[i]
                
print(b)
print(max(b))
        
    