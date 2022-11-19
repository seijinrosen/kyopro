from collections import defaultdict
from typing import Callable, DefaultDict, List, TypeVar, Union

_T = TypeVar("_T")


def constant_factory(value: _T) -> Callable[[], _T]:
    return lambda: value


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
QUERIES = [map(int, input().split()) for _ in range(Q)]

data: Union[List[int], DefaultDict[int, int]] = A

for query in QUERIES:
    q = next(query)

    if q == 1:
        data = defaultdict(constant_factory(next(query)))
    elif q == 2:
        data[next(query) - 1] += next(query)
    elif q == 3:
        print(data[next(query) - 1])
