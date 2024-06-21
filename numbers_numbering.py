a=[3,4,9,7,9,8,3,8,6,4,3,5]
b=[]
for i in a:
    if(i not in b):
        b.append(i)
for i in b:
    print(i,"-",a.count(i))
                                                             