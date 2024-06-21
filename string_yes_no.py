n=int(input())
m=[]
for i in range(n):
    m.append(list(input()))
s=input()
for i in range(len(s)):
    if s[i] not in m[i%n]:
        print("no")
        f=1
        break
    else:
        m[i].remove(s[i])
if(f==0):
    print("yes")