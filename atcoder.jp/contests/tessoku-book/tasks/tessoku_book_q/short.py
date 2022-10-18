N,A,B=[[*map(int,x.split())]for x in open(0)]
d=[0,A[0]]
for i in range(N[0]-2):d+=[min(d[i+1]+A[i+1],d[i]+B[i])]
r=[p:=N[0]]
while 1<p:r+=[p:=p-(d[p-2]+A[p-2]!=d[p-1])-1]
print(len(r),*r[::-1])