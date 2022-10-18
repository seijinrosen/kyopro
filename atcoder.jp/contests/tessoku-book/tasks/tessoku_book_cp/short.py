a=abs
N,*H=map(int,open(0).read().split())
d=[0,0,a(H[1]-H[0])]
for i in range(2,N):d+=[min(d[i]+a(H[i-1]-H[i]),d[i-1]+a(H[i-2]-H[i]))]
r=[p:=N]
while 1<p:r+=[p:=p-(d[p-1]+a(H[p-2]-H[p-1])!=d[p])-1]
print(len(r),*r[::-1])