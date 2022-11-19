N,K,*A=map(int,open(0).read().split())
print(*A[K:]+[0]*min(N,K))