a=[]
b=[]
c=[]
for i in range(1,1000001):
  if i%2==0:
    a.append(i)
  if i%3==0:
    b.append(i)
  if i%5==0:
    c.append(i)
d=a+b+c
s=set(d)
d=list(s)
fo=open("ans.txt","w")
fo.write(str(d))
fo.close()