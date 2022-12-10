N,t,*A=map(int,open(i:=0).read().split())
t%=sum(A)
while A[i]<t:t-=A[i];i+=1
print(i+1,t)