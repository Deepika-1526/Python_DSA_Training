def fun(i, j, c, n, m, vi):
    if i < 0 or i >= n or j < 0 or j >= m:  
        return c
    if i == n - 1 and j == m - 1:  
        c += 1
        return c
    vi.append((i, j))
    if (i - 1, j) not in vi:
        c = fun(i - 1, j, c, n, m, vi)
    if (i, j - 1) not in vi:
        c = fun(i, j - 1, c, n, m, vi)
    if (i + 1, j) not in vi:
        c = fun(i + 1, j, c, n, m, vi)
    if (i, j + 1) not in vi:
        c = fun(i, j + 1, c, n, m, vi)
    vi.pop()
    return c
n = 3  
m = 3  
c = 0  
vi = []  
result = fun(0, 0, c, n, m, vi)
print(result)
