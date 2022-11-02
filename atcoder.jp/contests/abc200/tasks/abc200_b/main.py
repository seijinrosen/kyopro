from itertools import islice
from typing import Callable, Iterable, Iterator, TypeVar, Union

_T = TypeVar("_T")
_U = TypeVar("_U")


# more-itertools
def iterate(func: Callable[[_T], _T], start: _T) -> Iterator[_T]:
    # https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.iterate
    while True:
        yield start
        start = func(start)


def nth(iterable: Iterable[_T], n: int, default: _U = None) -> Union[_T, _U]:
    # https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.nth
    return next(islice(iterable, n, None), default)


def func(n: int) -> int:
    if n % 200 == 0:
        return n // 200
    return 1000 * n + 200


N, K = map(int, input().split())

ans = nth(iterate(func, N), K)
print(ans)
