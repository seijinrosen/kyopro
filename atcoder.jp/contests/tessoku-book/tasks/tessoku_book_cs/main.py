from itertools import tee
from typing import Iterable, TypeVar

_T = TypeVar("_T")


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


S = input()
T = input()

N = len(S)
M = len(T)
dp = [range(M + 1)]

for s in S:
    row = [dp[-1][0] + 1]
    for (a, b), t in zip(pairwise(dp[-1]), T):
        row += [min(b + 1, row[-1] + 1, a + (s != t))]
    dp += [row]

ans = dp[N][M]
print(ans)
