'''
ip:
  360 days in a yr
  every month 30 days
  every week  6days--->5 weeks per month
  
  65476
  ?y ?m ?w ?d

consider every year has 360 days, every month has 30 days,every week has 6 days
i/p: 360 30 6
     65476
     y? m? w? d?
'''
days=int(input())
y=days//360
m=(days%360)//30
w=(days%30)//6
d=days%6
print(y,m,w,d,end=' ')