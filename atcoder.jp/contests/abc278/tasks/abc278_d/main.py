from collections import defaultdict
from typing import Callable, DefaultDict, TypeVar

_T = TypeVar("_T")


def constant_factory(value: _T) -> Callable[[], _T]:
    return lambda: value


N = int(input())
A = map(int, input().split())
Q = int(input())
QUERIES = (map(int, input().split()) for _ in range(Q))

d: DefaultDict[int, int] = defaultdict(int, enumerate(A))

for query in QUERIES:
    q = next(query)

    if q == 1:
        d = defaultdict(constant_factory(next(query)))
    elif q == 2:
        d[next(query) - 1] += next(query)
    elif q == 3:
        print(d[next(query) - 1])
