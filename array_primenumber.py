'''def is_prime(num):
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True
arr = [14,16,20,22]
primes_sum = 0

for i in range(len(arr) - 1):
  left = arr[i] + 1 
  right = arr[i + 1] - 1 
  largest_prime = None
  for num in range(right, left - 1, -1):  
    if is_prime(num):
      largest_prime = num
      break
  if largest_prime:
    primes_sum += largest_prime

print(primes_sum)'''

def is_prime(x):
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1
def lprime(n,m):
    for i in range(m-1,n,-1):
        if (is_prime(i)):
            return i
    return 0
a=list(map(int,input().split()))
s=0

for i in range(len(a)-1):
    s=s+lprime(a[i],a[i+1])
print(s)