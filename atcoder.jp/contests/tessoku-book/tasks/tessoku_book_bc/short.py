from bisect import*
L=[]
for r in[*open(0)][1:]:
 i=bisect_left(L,x:=int(r[2:]))
 if"2">r[0]:insort(L,x)
 elif"3">r[0]:L.pop(i)
 else:print(L[i]if i<len(L)else-1)