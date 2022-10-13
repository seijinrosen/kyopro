from typing import Any, Tuple, TypeVar

_T = TypeVar("_T")


def fst(x: Tuple[_T, Any]) -> _T:
    return x[0]


def snd(x: Tuple[Any, _T]) -> _T:
    return x[1]


N = int(input())
A = list(map(int, input().split()))

ans = fst(sorted(enumerate(A, start=1), key=snd)[-2])
print(ans)
