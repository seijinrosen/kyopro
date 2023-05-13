from functools import reduce
from itertools import tee
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
MOD = 10**9 + 7


def func(x: int, y: int) -> int:
    return (x * (y + 1)) % MOD


def solve() -> int:
    return reduce(func, diff([0, *sorted(A)]), 1)


print(solve())
