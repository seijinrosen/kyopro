from functools import reduce
from itertools import product
from operator import mul
from typing import Iterable


def prod(iterable: Iterable[int]) -> int:
    return reduce(mul, iterable)


A, B, C, D = map(int, input().split())

ans = max(map(prod, product([A, B], [C, D])))
print(ans)
