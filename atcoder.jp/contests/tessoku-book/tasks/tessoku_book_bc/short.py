from bisect import*
l=[]
for _ in range(int(input())):
 q,x=map(int,input().split())
 i=bisect_left(l,x)
 if q<2:l.insert(i,x)
 elif q<3:l.pop(i)
 else:print(l[i]if i<len(l)else-1)