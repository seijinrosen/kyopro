from itertools import accumulate, tee
from typing import Iterable, Iterator, TypeVar

_T = TypeVar("_T")


def diff(iterable: Iterable[int]) -> Iterator[int]:
    return (y - x for x, y in pairwise(iterable))


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


N, *A = map(int, open(0).read().split())


def func(a: int, b: int) -> int:
    return (a + b) % 360


def solve() -> int:
    acc = [0, *accumulate(A, func), 360]
    return max(diff(sorted(acc)))


print(solve())
