n,k=input().split()
s=input().split()
k=int(k)
a=[]
l=len(s)
for i in range(len(s)):
  if(i%2!=0):
    a.append(i)
b=a[k-1]
print(b)    
