N,*X=map(int,open(0).read().split())
A=X[:N-1]
B=X[N-1:]
d=[0,A[0]]
for i in range(1,N-1):d.append(min(d[i]+A[i],d[i-1]+B[i-1]))
r=[p:=N]
while 1<p:r.append(p:=p-(d[p-2]+A[p-2]!=d[p-1])-1)
print(len(r),*r[::-1])