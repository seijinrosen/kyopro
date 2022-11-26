N,M,*A=map(int,open(0).read().split())
C=[0]*M
for a in A:C[a%M]+=1
print(sum(x*(x-1)//2for x in C))