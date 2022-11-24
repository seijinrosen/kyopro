N,L,K,*A=map(int,open(0).read().split())
l=1
r=L
while 1<r-l:
 m=(l+r)//2;c=n=x=0
 for a in A:
  if m<=a-n:c+=1;n=a
  if c==K:x=m<=L-n;break
 if x:l=m
 else:r=m
print(l)