N,*H=map(int,open(0).read().split())
d=[0,abs(H[1]-H[0])]
for i in range(2,N):d+=[min(d[i-1]+abs(H[i-1]-H[i]),d[i-2]+abs(H[i-2]-H[i]))]
r=[p:=N]
while 1<p:r+=[p:=p-(d[p-2]+abs(H[p-2]-H[p-1])!=d[p-1])-1]
print(len(r),*r[::-1])