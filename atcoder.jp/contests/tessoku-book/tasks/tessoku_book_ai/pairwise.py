from itertools import tee
from typing import Iterable, TypeVar

_T = TypeVar("_T")


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


N = int(input())
A = list(map(int, input().split()))

dp = [A]
for i in reversed(range(N - 1)):
    if i % 2 == 0:
        row = [*map(max, pairwise(dp[-1]))]
    else:
        row = [*map(min, pairwise(dp[-1]))]
    dp.append(row)

ans = dp[-1][0]
print(ans)
