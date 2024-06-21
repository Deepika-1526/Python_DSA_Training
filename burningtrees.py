'''
ip:
  1->trees
  0->land
  6
  0 1 1 1 0 1                               (i-1,j)
  0 1 0 1 0 0                                
  1 0 1 1 0 0                        (i,j-1)  (i,j)   (i,j+1)
  0 0 0 1 1 1
  1 1 0 0 0 1                                (i+1,j)
  1 1 1 0 1 0
  
  4 6-->4th row 5th col
  fire does not catch diagonally
  op:8

'''

def fun(arr,n,r,c):
    if r<0 or c<0 or r>=n or c>=n or arr[r][c]!=1:
        return

    if arr[r][c]==1:
        arr[r][c]=2
        fun(arr,n,r-1,c)#top
        fun(arr,n,r,c-1)#left
        fun(arr,n,r,c+1)#right
        fun(arr,n,r+1,c)#bottom
        
        
n=int(input())
arr=[]
for i in range(n):
    col=[]
    for j in range(n):
        val=int(input())
        col.append(val)
    arr.append(col)
print(arr)
r=int(input())
c=int(input())

fun(arr,n,r,c)
print(arr)

ct=0
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            ct+=1
print(ct)


        

