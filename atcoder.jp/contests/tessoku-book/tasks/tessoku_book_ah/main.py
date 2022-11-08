from functools import reduce
from operator import xor
from typing import Iterable, Set


def mex(st: Set[int]) -> int:
    return next(i for i in range(len(st) + 1) if i not in st)


def nim(iterable: Iterable[int]) -> bool:
    return 0 < reduce(xor, iterable)


N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

MAX_A = max(A)
grundy = [0] * (MAX_A + 1)

for i in range(X, MAX_A + 1):
    grundy[i] = mex({grundy[i - x] for x in [X, Y] if x <= i})

ans = nim(grundy[a] for a in A)
print("First" if ans else "Second")
