from typing import Iterable


def sum_2d(table: Iterable[Iterable[int]]) -> int:
    return sum(map(sum, table))


H, W = map(int, input().split())
S = [[c == "#" for c in input()] for _ in range(H)]

ans = sum_2d(S)
print(ans)
