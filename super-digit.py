def summ(n):
  s=0
  t=n
  while(n!=0 or s>9):
    if (n==0):
      n=s
      s=0
    r=n%10
    s=s+r
    n=n//10
  return s



n=int(input("enter number"))
k=int(input("enter key"))
a=str(n)
n=a*k
print(n)
print(summ(int(n)))
