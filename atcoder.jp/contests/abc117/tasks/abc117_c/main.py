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


N, M, *X = map(int, open(0).read().split())


ans = sum(sorted(diff(sorted(X)))[: max(0, M - N)])


print(ans)
