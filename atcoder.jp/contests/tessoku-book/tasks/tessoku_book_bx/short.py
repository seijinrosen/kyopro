from bisect import*
N,W,L,R,*Y=map(int,open(0).read().split())
X=[0,*Y,W]
d=[0,1]
for x in X[1:]:a=d[bisect(X,x-L)]-d[bisect_left(X,x-R)];d+=[d[-1]+a]
print(a%(10**9+7))