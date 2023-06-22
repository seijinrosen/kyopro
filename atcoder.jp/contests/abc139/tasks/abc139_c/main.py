from itertools import tee
from typing import Iterable, TypeVar

_T = TypeVar("_T")


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


N, *H = map(int, open(0).read().split())


def solve() -> int:
    ans = 0
    cnt = 0

    for a, b in pairwise(H):
        if b <= a:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0

    return ans


print(solve())
