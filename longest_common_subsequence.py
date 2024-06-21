s1 = "abcd"
s2 = "axbdc"
u = len(s1)
v = len(s2)
m = []

for i in range(len(s1) + 1):
    l = [0] * (len(s2) + 1)
    m.append(l)


for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            m[i][j] = m[i - 1][j - 1] + 1
        else:
            m[i][j] = max(m[i][j - 1], m[i - 1][j])

u = len(s1)
v = len(s2)
s = []

while u != 0 and v != 0:
    if s1[u - 1] == s2[v - 1]:
        s.append(s1[u - 1])
        u -= 1
        v -= 1
    elif m[u][v - 1] >= m[u - 1][v]:
        v -= 1
    else:
        u -= 1

s.reverse()


s_str = ''.join(s)
print(s_str)
