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


N = int(input())
S = map(int, input().split())

ans = diff((0, *S))
print(*ans)
