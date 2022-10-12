import math

N, D = map(int, input().split("/"))

gcd = math.gcd(N, D)
print(N // gcd, "/", D // gcd, sep="")
