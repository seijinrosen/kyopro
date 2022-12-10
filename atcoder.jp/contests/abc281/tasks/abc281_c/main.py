N,t,*A=map(int,open(0).read().split())
t%=sum(A)
for i,a in enumerate(A,1):
 if t<a:print(i,t);break
 t-=a