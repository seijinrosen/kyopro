from itertools import combinations
from typing import Iterable, List, TypeVar

_T = TypeVar("_T")


def inversion(iterable: Iterable[int]) -> int:
    """転倒数
    >>> inversion([2, 3, 4, 1])
    3
    >>> inversion([3, 1, 2, 4])
    2
    """
    return sum(y < x for x, y in combinations(iterable, 2))


def transpose(table: Iterable[Iterable[_T]]) -> List[List[_T]]:
    return list(map(list, zip(*table)))


N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

X = (p for row in P for p in row if p)
Y = (p for col in transpose(P) for p in col if p)

ans = inversion(X) + inversion(Y)
print(ans)
