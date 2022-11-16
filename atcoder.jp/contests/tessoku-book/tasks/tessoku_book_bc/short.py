from bisect import*
l=[]
for r in[*open(0)][1:]:
 i=bisect_left(l,x:=int(r[2:]))
 if r[0]<"2":l.insert(i,x)
 elif r[0]<"3":l.pop(i)
 else:print(l[i]if i<len(l)else-1)