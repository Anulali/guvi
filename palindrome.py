num=int(input(" "))
temp=num
r=0
while(num>0):
  x=num%10
  r=r*10+x
  num=num//10
if(temp==r):
  print("yes")
else:
  print("no")    
