N,*A=map(int,open(0).read().split())
print(sum((A[x]+A[y])%100<1for x in range(N)for y in range(x+1,N)))