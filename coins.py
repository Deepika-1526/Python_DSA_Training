'''li = [1, 3, 4, 5]
val = 17
dp = [[0] * (val + 1) for i in range(len(li) + 1)]

for i in range(1, len(li) + 1):
    for j in range(val + 1):
        if j == 0:
            dp[i][j] = 0  
        elif i == 1:
            dp[i][j] = j  
        else:
            if j < li[i - 1]:
                dp[i][j] = dp[i - 1][j]  
            else:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - li[i - 1]])

result = dp[len(li)][val]
print(result) '''


def fun():
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range (1,n+1):
            if(j>=i):
                if(l1[j-i]!=-1):
                    if(l1[j]!= -1):
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1[-1])


l=[3,4]
n=5
fun()

