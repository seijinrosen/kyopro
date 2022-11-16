from bisect import*
L=[]
for r in[*open(0)][1:]:
 i,*X=bisect(L,x:=int(r[2:])),
 if"2">r:insort(L,x)
 else:
  if i<len(L):X+=L[i]-x,
  if i:X+=x-L[i-1],
  print(min(X or[-1]))