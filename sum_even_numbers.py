'''def sum_even_numbers(n):
    if n < 2:
        return 0
    elif n % 2 == 0:
        return n + sum_even_numbers(n - 2)
    else:
        return sum_even_numbers(n - 1)
result = sum_even_numbers(10)
print(result)'''


'''def fa(x):
    if(x==0):
        return 0
    return x+ fa(x-2)
print(fa(10))'''


def fa(x):
    if(x==0):
        return 0
    return x+ fa(x-2)
print(fa(10))

n=14
if(n%2==0):
    print(fa(n))
else:
    print(fa(n-1))
