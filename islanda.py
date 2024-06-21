def fun(i, j, c):
    if i < 0 or j < 0 or i >= n or j >= n or a[i][j] != 1:
        return c
    a[i][j] = 2
    c += 1
    c = fun(i, j-1, c)
    c = fun(i, j+1, c)
    c = fun(i-1, j, c)
    c = fun(i+1, j, c)
    return c

a = [[1, 0, 0, 1], [0, 0, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1]]
n = 4
co = 0
k = 0
for i in range(4):
    for j in range(4):
        if a[i][j] == 1:
            k = fun(i, j, 0)
            co += 1
print(co, k)