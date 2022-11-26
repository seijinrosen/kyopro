from typing import Iterable, List, TypeVar

_T = TypeVar("_T")


def transpose(table: Iterable[Iterable[_T]]) -> List[List[_T]]:
    return list(map(list, zip(*table)))


H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

SS = transpose(S)
TT = transpose(T)

ans = sorted(SS) == sorted(TT)
print("Yes" if ans else "No")
