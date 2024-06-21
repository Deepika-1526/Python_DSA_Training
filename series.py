n=5
k=1
for i in range(5):
    for j in range(5):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end="")
        else:
            print(k,end="")
            k=k+1
    print()

