'''def sub_string(s):
    start = 0
    max_length = 0
    max_substring = ""
    set = {}

    for i in range(len(s)):
        char = s[i]
        if char in set and set[char] >= start:
            start = set[char] + 1
        set[char] = i
        if i - start + 1 > max_length:
            max_length = i - start + 1
            max_substring = s[start:i + 1]

    return max_substring

str = "abfgresagtyuiofde"
print(sub_string(str))'''

#using dictionary
'''a = "abfgresagtyuiofd"
d = {}
s = ""
m = 0
i = 0

while i < len(a):
    while i < len(a):
        if (a[i] not in s):
            s = s + a[i]
            d[s[i]] = i
        else:
            if len(s) > m:
                m = len(s)
                s = ""
                break
    i = d[s[i]]+1

print(m)'''

a = "abfgresagtyuiofd"
d = {}
s = ""
m = 0
i = 0

while i < len(a):
    if a[i] not in s:
        s += a[i]
        d[a[i]] = i
    else:
        if len(s) > m:
            m = len(s)
        i = d[a[i]] + 1
        s = ""
        d = {}
    i += 1

if len(s) > m:
    m = len(s)

print(m)

