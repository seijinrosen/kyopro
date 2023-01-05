from itertools import tee
from typing import Iterable, List, TypeVar

_T = TypeVar("_T")


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def is_weak1(xs: List[int]) -> bool:
    return len(set(xs)) == 1


def is_weak2(xs: List[int]) -> bool:
    return all((x + 1) % 10 == y for x, y in pairwise(xs))


XS = list(map(int, input()))
print("Weak" if is_weak1(XS) or is_weak2(XS) else "Strong")
