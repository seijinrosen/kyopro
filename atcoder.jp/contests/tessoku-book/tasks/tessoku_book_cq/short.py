N,S,*A=map(int,open(0).read().split())
d=[[1]+[0]*S]
for a in A:d+=[[a<=j and d[-1][j-a]or d[-1][j]for j in range(S+1)]]
if d[N][S]<1:print(-1);exit()
j=S
c=[]
for i in range(N):
 if d[N-i-1][j]<1:c+=[N-i];j-=A[N-i-1]
print(len(c),*c[::-1])