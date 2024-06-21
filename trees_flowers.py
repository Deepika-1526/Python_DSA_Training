'''l=[]
n=int(input())
for i in range(n):
    r=[]
    for j in range(n):
        ele=int(input())
        r.append(ele)
    l.append(r)
print(l,end=" ")
def fire(l,i,j):
    if  i>=0 and j>=0 and i<len(l) and j<len(l):
        if l[i][j]==0:
            return 0
        
        elif  l[i][j]==1:
            l[i][j]=2
            fire(l,i-1,j)
            fire(l,i,j-1)
            fire(l,i,j+1)
            fire(l,i+1,j)


i=1
j=1
fire(l,i,j)
c=0
for i in range(len(l)):
    for j in range(len(l)):
        if l[i][j]==1:
            c+=1
print()
print(l)
print(c)'''

def fun(i, j):
    if i < 0 or j < 0 or i >= n or j >= n or a[i][j] != 1:
        return
    if a[i][j] == 1:
        a[i][j] = 2
    fun(i-1, j)
    fun(i, j-1)
    fun(i+1, j)
    fun(i, j+1)
    return


n = int(input("Enter the size of the matrix: "))
a = []
for i in range(n):
    row = []
    for j in range(n):
        ele = int(input())
        row.append(ele)
    a.append(row)
print("Initial matrix:")
for row in a:
    print(row)

i, j = 1, 1


fun(i, j)


c = 0
for row in a:
    c += row.count(1)
print("Modified matrix:")
for row in a:
    print(row)
print("Number of remaining 1s:", c)
