N,*A=map(int,open(0).read().split())
print(sum((A[x]+b)%100<1for x in range(N)for b in A[x+1:]))