n1,n2=input().split()
x=int(n1)
z=int(n2)
for i in range(x+1,z):
  if(i%2!=0):
    print(i,end=" ")
