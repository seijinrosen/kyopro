N,L,K,*A=map(int,open(0).read().split())
l=1
r=L
while 1<r-l:
 m=(l+r)//2;c=n=0
 for a in A:
  if m<=a-n and m<=L-a:c+=1;n=a
 if c<K:r=m
 else:l=m
print(l)