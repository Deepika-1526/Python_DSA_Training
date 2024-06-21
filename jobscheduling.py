'''a = [5, 6, 5, 4, 11, 2]
nums = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
for i in range (len(a)):
    d=[(nums[i][0],nums[i][1],a[i])]
    d.sort(key=lambda x:x[1])
def amount(d,index=0,sum=0,end=0):
    if index == len(d):
        return sum
    if d[index][0] >= end:
        return max(amount(d,index+1,sum+d[index][2],d[index][1]),
                   amount(d,index+1,sum,end))
    else:
        return amount(d,index+1,sum,end)

max_amount=amount(d)
print(max_amount)'''

nums=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=a.copy()
for i in range(1,len(nums)):
    for j in range(0,i):
        if nums[j][1]<=nums[i][0] and b[i]<b[j]+a[i]:
            b[i]=b[j]+a[i]
print(max(b))
