a=input()
n=int(input())
s=""
for i in range(n):
    b=input()
    if b[0]=='L':
        s+=a[-int(b[2])]
    else:
        s+=a[-int(b[2])]
s=list(s)
s.sort()
b=[]
for i in range(len(a)-n+1):
    t=sorted(list(a[i:n+i]))
    b.append(t)
for i in b:
    if i==s:
        print("yes")
        break
