import math
x,*A=map(int,[*open(0)][1].split())
for a in A:x=math.gcd(x,a)
print(x)