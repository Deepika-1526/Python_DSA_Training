a = [1, 5, 8, 9]
b = [2, 7, 9, 10, 14]
c = []
i, j = 0, 0

# Merge the two lists
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

# Append remaining elements of a (if any)
while i < len(a):
    c.append(a[i])
    i += 1

# Append remaining elements of b (if any)
while j < len(b):
    c.append(b[j])
    j += 1

print(c)
