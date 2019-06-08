n,k=input().split()
s=list(map(int,input().split()))
k=int(k)
n=int(n)
a=[]

for i in range(len(s)):
  if(s[i]%2!=0):
    a.append(s[i])
print(a[k-1]) 
