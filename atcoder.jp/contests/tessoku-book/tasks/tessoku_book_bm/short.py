N,*A=map(int,open(0).read().split())
d=[0]*N
for i in range(N-1)[::-1]:d[A[i]-1]+=d[i+1]+1
print(*d)