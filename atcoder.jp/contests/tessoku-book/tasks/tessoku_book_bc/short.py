from bisect import bisect_left as b
l=[]
for _ in range(int(input())):
 q,x=map(int,input().split())
 i=b(l,x)
 if q<2:l.insert(i,x)
 if q==2:l.pop(i)
 if q>2:print(l[i]if i<len(l)else-1)