import math
f=math.factorial
N,R=map(int,input().split())
print(f(N)//f(R)//f(N-R)%(10**9+7))