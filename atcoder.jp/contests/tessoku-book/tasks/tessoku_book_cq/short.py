n,s,*A=map(int,open(0).read().split())
d=[[1]+[0]*s]
for a in A:d+=[[a<=j and d[-1][j-a]or d[-1][j]for j in range(s+1)]]
if d[n][s]<1:print(-1);exit()
c=[]
while n:
 if d[n-1][s]<1:c+=[n];s-=A[n-1]
 n-=1
print(len(c),*c[::-1])