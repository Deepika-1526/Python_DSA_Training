def fun(i,j,n,m,c,k,p,vi):
    if i < 0 or j < 0 or i >= n or j >= m or (i==k and j==p):
        return c
    if(i==n-1 and j==m-1):
        c=c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        c=fun(i-1,j,n,m,c,k,p,vi)#top
        
    if((i,j-1) not in vi):
        c=fun(i,j-1,n,m,c,k,p,vi)
        
    if((i,j+1) not in vi):
        c=fun(i,j+1,n,m,c,k,p,vi)
        
    if((i+1,j) not in vi):
        c=fun(i+1,j,n,m,c,k,p,vi)
    print(vi.pop(),end=" ")
    return c

r=int(input())
c=int(input())
l=[]
for i in range(r):
    k=['-']*c
    l.append(k)
    
print(l)
t=fun(0,0,r,c,0,1,2,[])
print()
print(t)