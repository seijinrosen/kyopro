from itertools import tee
from typing import Iterable, Iterator, Tuple, TypeVar

_T = TypeVar("_T")


def triplewise(iterable: Iterable[_T]) -> Iterator[Tuple[_T, _T, _T]]:
    # https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.triplewise
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


N, K, *T = map(int, open(0).read().split())


ans = next((i for i, x in enumerate(triplewise(T), 3) if sum(x) < K), -1)


print(ans)
