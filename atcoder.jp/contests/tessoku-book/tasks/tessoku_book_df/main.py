from functools import reduce
from itertools import chain
from operator import xor
from typing import List, Tuple

N, H, W = map(int, input().split())
AB: List[Tuple[int, int]] = [
    tuple(int(x) - 1 for x in input().split()) for _ in range(N)
]

nim = reduce(xor, chain.from_iterable(AB))
print("Second" if nim == 0 else "First")
