def kth_factor(n,k):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    
  
    factors.sort()

    if k <= len(factors):
        return factors[k - 1]
    else:
        return -1  


n=int(input())
k=int(input())
result = kth_factor(n, k)
print(result)
