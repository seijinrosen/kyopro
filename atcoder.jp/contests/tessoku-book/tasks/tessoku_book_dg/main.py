from functools import reduce
from operator import xor
from typing import Iterable


def nim(iterable: Iterable[int]) -> bool:
    return 0 < reduce(xor, iterable)


input()
A = map(int, input().split())

grundy = [0, 0, 1, 1, 2]
ans = nim(grundy[a % 5] for a in A)

print("First" if ans else "Second")
