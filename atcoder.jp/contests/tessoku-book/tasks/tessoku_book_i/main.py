from itertools import accumulate
from typing import TypeVar

_T = TypeVar("_T")


def accumulate_2d(table: "list[list[int]]") -> "list[list[int]]":
    acc = [[*accumulate(row)] for row in table]
    return transpose([[*accumulate(column)] for column in transpose(acc)])


def transpose(table: "list[list[_T]]") -> "list[list[_T]]":
    return list(map(list, zip(*table)))


# input functions --------------------------------------------------------------
def input_int_tuple_list(n: int) -> "list[tuple[int, int, int, int]]":
    return [tuple(map(int, input().split())) for _ in range(n)]


H, W, N = map(int, input().split())
ABCD = input_int_tuple_list(N)


X = [[0] * (W + 1) for _ in range(H + 1)]
for a, b, c, d in ABCD:
    X[a - 1][b - 1] += 1
    X[a - 1][d] -= 1
    X[c][b - 1] -= 1
    X[c][d] += 1

acc = accumulate_2d(X)
ans = [row[:W] for row in acc[:H]]


for row in ans:
    print(*row)
