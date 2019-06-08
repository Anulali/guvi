n=int(input())
tem=n
c=0
while(n!=1):
  n=n//2
  c=c+1
x=2**c
if(tem==x):
  print("yes")
else:
  print("no")  

