a="MMFFMFFMFMFMFFMMFFMMF"
c=0
for i in a :
    if(i=='M'):
        c=c+1
    else:
        c=c-1
if c==0:
    print("0")
elif c==1:
    print("M")
else:
    print("F")


