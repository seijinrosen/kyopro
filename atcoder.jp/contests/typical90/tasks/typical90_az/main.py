from functools import reduce
from typing import List, Tuple

A: List[Tuple[int, int, int, int, int, int]] = [
    tuple(map(int, row.split())) for row in [*open(0)][1:]
]

MOD = 10**9 + 7
ans = reduce(lambda x, y: x * y % MOD, map(sum, A))

print(ans)
