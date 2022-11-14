from itertools import tee
from typing import Iterable, Iterator, Tuple, TypeVar

_T = TypeVar("_T")


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def triplewise(iterable: Iterable[_T]) -> Iterator[Tuple[_T, _T, _T]]:
    # https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.triplewise
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


N = int(input())
S = input()

ans = any(a == b == c for a, b, c in triplewise(S))
print("Yes" if ans else "No")
