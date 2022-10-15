from bisect import bisect_left
from itertools import product
from typing import Union


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

P = [a + b for a, b in product(A, B)]
Q = [c + d for c, d in product(C, D)]
Q.sort()

for p in P:
    pos1 = bisect_left(Q, K - p)
    if pos1 < N * N and Q[pos1] == K - p:
        ans = True
        break
else:
    ans = False

print(yes_no(ans))
