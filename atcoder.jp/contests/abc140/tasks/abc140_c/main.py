from itertools import tee
from typing import Iterable, TypeVar

_T = TypeVar("_T")


N, *B = map(int, open(0).read().split())


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def solve() -> int:
    A = [B[0], *map(min, pairwise(B)), B[-1]]
    return sum(A)


print(solve())
