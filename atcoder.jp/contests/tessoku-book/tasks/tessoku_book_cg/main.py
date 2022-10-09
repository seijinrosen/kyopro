from itertools import accumulate
from typing import TypeVar

_T = TypeVar("_T")


def accumulate_2d(table: "list[list[int]]") -> "list[list[int]]":
    acc = [[0, *accumulate(row)] for row in table]
    return transpose([[0, *accumulate(column)] for column in transpose(acc)])


def transpose(table: "list[list[_T]]") -> "list[list[_T]]":
    return list(map(list, zip(*table)))


# input functions --------------------------------------------------------------
def input_int_pair_list(n: int) -> "list[tuple[int, int]]":
    return [tuple(map(int, input().split())) for _ in range(n)]


def input_int_tuple_list(n: int) -> "list[tuple[int, int, int, int]]":
    return [tuple(map(int, input().split())) for _ in range(n)]


N = int(input())
XY = input_int_pair_list(N)
Q = int(input())
ABCD = input_int_tuple_list(Q)


graph = [[0] * 1500 for _ in range(1500)]
for x, y in XY:
    graph[x - 1][y - 1] += 1

acc = accumulate_2d(graph)

ans = [
    acc[c][d] - acc[c][b - 1] - acc[a - 1][d] + acc[a - 1][b - 1] for a, b, c, d in ABCD
]


print(*ans, sep="\n")
