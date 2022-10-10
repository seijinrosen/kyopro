from itertools import accumulate
from typing import TypeVar

_T = TypeVar("_T")


def accumulate_2d(table: "list[list[int]]") -> "list[list[int]]":
    acc = [[*accumulate(row)] for row in table]
    return transpose([[*accumulate(column)] for column in transpose(acc)])


def transpose(table: "list[list[_T]]") -> "list[list[_T]]":
    return list(map(list, zip(*table)))


N = int(input())
ABCD: "list[tuple[int, int, int, int]]" = [
    tuple(map(int, input().split())) for _ in range(N)
]


H, W = 1501, 1501

X = [[0] * W for _ in range(H)]
for a, b, c, d in ABCD:
    X[a][b] += 1
    X[c][d] += 1
    X[a][d] -= 1
    X[c][b] -= 1

acc = accumulate_2d(X)
ans = sum(sum(map(bool, row)) for row in acc)


print(ans)
