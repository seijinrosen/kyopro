from itertools import accumulate
from typing import TypeVar

_T = TypeVar("_T")


def accumulate_2d(table: "list[list[int]]") -> "list[list[int]]":
    acc = [[0, *accumulate(row)] for row in table]
    return transpose([[0, *accumulate(column)] for column in transpose(acc)])


def transpose(table: "list[list[_T]]") -> "list[list[_T]]":
    return list(map(list, zip(*table)))


def input_int_tuple_list(n: int) -> "list[tuple[int, int, int, int]]":
    return [tuple(map(int, input().split())) for _ in range(n)]


H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
ABCD = input_int_tuple_list(Q)


acc = accumulate_2d(X)
ans = [
    acc[c][d] - acc[a - 1][d] - acc[c][b - 1] + acc[a - 1][b - 1] for a, b, c, d in ABCD
]


print(*ans, sep="\n")
