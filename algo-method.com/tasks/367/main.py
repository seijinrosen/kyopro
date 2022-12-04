from typing import Callable, TypeVar

_T = TypeVar("_T")


def apply_n_times(func: Callable[[_T], _T], start: _T, n: int) -> _T:
    for _ in range(n):
        start = func(start)
    return start


N, M = map(int, input().split())


def func(x: float) -> float:
    return apply_n_times(lambda n: n * x + 1, N + 1, 5)


lo = 0
hi = M
while 1e-3 < hi - lo:
    mid = (lo + hi) / 2
    if func(mid) < M:
        lo = mid
    else:
        hi = mid


print(lo)
