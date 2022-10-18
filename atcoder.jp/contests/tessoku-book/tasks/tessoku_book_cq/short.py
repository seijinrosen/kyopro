N,s,*A=map(int,open(0).read().split())
d=[[1]+[0]*s]
for a in A:d+=[[a<=j and d[-1][j-a]or d[-1][j]for j in range(s+1)]]
if d[N][s]<1:print(-1);exit()
c=[]
for i in range(N):
 if d[N-i-1][s]<1:c+=[N-i];s-=A[N-i-1]
print(len(c),*c[::-1])