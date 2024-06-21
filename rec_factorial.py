def fa(x):
    if(x==1):
        return 1
    return x* fa(x-1)
print(fa(5))