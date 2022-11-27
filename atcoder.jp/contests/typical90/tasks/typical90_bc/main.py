from itertools import combinations

N, P, Q, *A = map(int, open(0).read().split())

B = [a % P for a in A]
ans = sum(
    a * b % P * c % P * d % P * e % P == Q for a, b, c, d, e in combinations(B, 5)
)

print(ans)
