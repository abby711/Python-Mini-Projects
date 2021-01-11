import random

d=['0','1','2','3','4','5','6','7','8','9']
a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
aa=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
sp=['!','@','#','$','%','^','&','*','(',')']

def asap(n,c):
  g=''
  if c==1:
    g=g.join(random.sample(d,n))
    return g
  elif c==2:
    g=g.join(random.sample(a,n))
    return g
  elif c==3:
    g=g.join(random.sample(aa,n))
    return g
  else:
    g=g.join(random.sample(sp,n))
    return g




l=int(input("enter length of password"))

x=int(input("enter number of digits"))

y=int(input("enter number of upper case alphabets"))
z=int(input("enter number of lower case alphabets"))
w=int(input("enter number of special characters"))


r=asap(y,2)
q=asap(x,1)
s=asap(z,3)
t=asap(w,4)
res=r+q+s+t

print(res)
