from functools import reduce
from operator import xor
from typing import Iterable


def nim(iterable: Iterable[int]) -> bool:
    return 0 < reduce(xor, iterable)


N = int(input())
A = map(int, input().split())

print("First" if nim(A) else "Second")
