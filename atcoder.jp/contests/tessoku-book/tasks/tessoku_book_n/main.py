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
Q = {c + d for c, d in product(C, D)}

ans = any(K - p in Q for p in P)
print(yes_no(ans))
