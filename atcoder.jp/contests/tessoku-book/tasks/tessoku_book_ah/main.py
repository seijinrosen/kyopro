from functools import reduce
from operator import xor
from typing import Set


def mex(st: Set[int]) -> int:
    return next(i for i in range(len(st) + 1) if i not in st)


N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

MAX_A = max(A)
grundy = [0] * (MAX_A + 1)

for i in range(X, MAX_A + 1):
    grundy[i] = mex({grundy[i - x] for x in [X, Y] if x <= i})

nim = reduce(xor, (grundy[a] for a in A))
print("Second" if nim == 0 else "First")
