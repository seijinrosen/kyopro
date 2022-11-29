from itertools import tee
from typing import Iterable, Iterator, List, Tuple, TypeVar

_T = TypeVar("_T")


def diff(iterable: Iterable[int]) -> Iterator[int]:
    return (y - x for x, y in pairwise(iterable))


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


N, Q = map(int, input().split())
A = map(int, input().split())
LRV: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(Q)]

B = [0, *diff(A), 0]
now = sum(abs(b) for b in B)

for l, r, v in LRV:
    now -= abs(B[l - 1]) + abs(B[r])
    if 1 < l:
        B[l - 1] += v
    if r < N:
        B[r] -= v
    now += abs(B[l - 1]) + abs(B[r])
    print(now)
