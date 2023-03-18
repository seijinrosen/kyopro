from functools import reduce
from itertools import combinations
from operator import mul
from typing import Iterable


def prod(iterable: Iterable[int], *, start: int = 1, mod: int = 0) -> int:
    if mod:
        return reduce(lambda a, b: a * b % mod, iterable, start)
    return reduce(mul, iterable, start)


N = int(input())
S = [input() for _ in range(N)]


march = [[s for s in S if s[0] == ch] for ch in "MARCH"]
ans = sum(prod(map(len, comb)) for comb in combinations(march, 3))


print(ans)
