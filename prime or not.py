n=int(input())
while(1):
    c=0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            c=c+1
            break
    if(c==0):
        print(n)
        break
    else:
        n=n+1
    

