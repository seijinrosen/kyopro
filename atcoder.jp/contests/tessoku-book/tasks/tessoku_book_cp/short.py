a=abs
n,*H=map(int,open(0).read().split())
d=[0,0,a(H[1]-H[0])]
for i in range(2,n):d+=[min(d[i]+a(H[i-1]-H[i]),d[i-1]+a(H[i-2]-H[i]))]
r=[n]
while 1<n:r+=[n:=n-(d[n-1]+a(H[n-2]-H[n-1])!=d[n])-1]
print(len(r),*r[::-1])