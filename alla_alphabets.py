#lowercase
'''a=input()
d={}
for i in a:
    if(i.islower()):
        if(i not in d):
            d[i]=1
print(d)'''
#set
a=input()
d=set()
for i in a:
    if(i.islower()):
        if(i not in d):
            d.add(i)
print(d)

#dictionaries
'''a= input()
d=[0]*26

for i in a:
    if(i.islower()):
        d[ord(i)-97]+=1
print(d)'''

#all alphabets

'''a= input()
d=[0]*26

for i in a:
    if(i.islower()):
        d[ord(i)-97]+=1
print(all(d))'''


