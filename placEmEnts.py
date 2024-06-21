'''a="placements"
b=[]
for i in a:
    if (i.islower()):
        if(i in 'aeiou'):
            print(i.upper())
        else:
            print(i)
    elif(i.isupper):
        if(i in 'AEIOU'):
            print(i.lower())
        else:
            print(i)'''
a = "placements"
b = []

for i in a:
    if i.islower():
        if i in 'aeiou':
            b.append(i.upper())
        else:
            b.append(i)
    elif i.isupper():
        if i in 'AEIOU':
            b.append(i.lower())
        else:
            b.append(i)

print(''.join(b))
