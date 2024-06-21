'''
ip:
7262 sec
op:2h:1m:2

ip:500 sec
op:0h:8m:20sec

'''

n=int(input())
h=n//3600
s=n-(3600*h)
m=s//60
sec=s-(m*60)
print(f"{h}h:{m}m:{sec}sec")