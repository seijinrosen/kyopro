from typing import Iterable, List, TypeVar

_T = TypeVar("_T")


def transpose(table: Iterable[Iterable[_T]]) -> List[List[_T]]:
    return list(map(list, zip(*table)))


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

row_sum = [sum(row) for row in A]
col_sum = [sum(col) for col in transpose(A)]

for i in range(H):
    row = [row_sum[i] + col_sum[j] - A[i][j] for j in range(W)]
    print(*row)
