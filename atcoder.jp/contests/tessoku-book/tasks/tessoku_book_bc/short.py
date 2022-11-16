from bisect import*
L=[]
for r in[*open(0)][1:]:
 i=bisect_left(L,x:=int(r[2:]))
 if"2">r:insort(L,x)
 elif"3">r:L.pop(i)
 else:print(i<len(L)and L[i]or-1)