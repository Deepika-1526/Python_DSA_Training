encoded = [1, 2, 3]
first = 1 
a = [first]
for i in range(len(encoded)):
    a.append(a[i] ^ encoded[i])
print(a)
