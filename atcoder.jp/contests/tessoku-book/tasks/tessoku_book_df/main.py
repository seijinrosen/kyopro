from functools import reduce
from itertools import chain
from operator import xor
from typing import Iterable, List, Tuple


def nim(iterable: Iterable[int]) -> bool:
    return 0 < reduce(xor, iterable)


N, H, W = map(int, input().split())
AB: List[Tuple[int, int]] = [
    tuple(int(x) - 1 for x in input().split()) for _ in range(N)
]

ans = nim(chain.from_iterable(AB))
print("First" if ans else "Second")
