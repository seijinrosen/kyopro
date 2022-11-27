from typing import Callable, Iterable, Iterator, List, Tuple, TypeVar

_T = TypeVar("_T")
_S = TypeVar("_S")


def accumulate_with_initial(
    iterable: Iterable[_S], func: Callable[[_T, _S], _T], initial: _T
) -> Iterator[_T]:
    # https://docs.python.org/ja/3/library/itertools.html#itertools.accumulate
    total = initial
    yield total
    for element in iter(iterable):
        total = func(total, element)
        yield total


N = int(input())
CP: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
LR: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(Q)]


def acc(c: int) -> List[int]:
    return [
        *accumulate_with_initial(CP, lambda x, cp: x + (cp[0] == c) * cp[1], initial=0)
    ]


acc1 = acc(1)
acc2 = acc(2)

for l, r in LR:
    a = acc1[r] - acc1[l - 1]
    b = acc2[r] - acc2[l - 1]
    print(a, b)
