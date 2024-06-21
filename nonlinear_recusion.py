def fun(x):
    if(x==1):
        return 2
    if(x==2):
        return 3
    if(x==3):
        return 4
    return fun(x-2)+fun(x-1)+fun(x-3)+x
print(fun(8))