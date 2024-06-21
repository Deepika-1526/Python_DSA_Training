a=input().split(',')
s=''
for i in a:
    b=i.split(":")
    l = len(b[0])
    if(str(l) in b[1]):
        s=s+b[0][-1]
    else:
        for i in range(l-1,0,-1):
            if(str(i) in b[1]):
                s=s+b[0][i-1]
                break
        else:
            s=s+'x'
print(s)
                