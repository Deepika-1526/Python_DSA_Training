li=[]
res=[]
for i in range(6):
    li.append(int(input()))
for i in range(6):
    for j in range(i,6):
        if li[i]<li[j]:
            res.append(li[j]-li[i])
if res!=[]:
    print(max(res))
else:
    print(0)