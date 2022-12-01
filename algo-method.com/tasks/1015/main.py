from operator import itemgetter
from typing import Iterable, Tuple


class UnionFind:
    # https://algo-method.com/descriptions/136
    def __init__(self, n: int) -> None:
        self.par = [-1] * n
        self.rank = [0] * n

    def root(self, x: int) -> int:
        if self.par[x] == -1:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self, x: int, y: int) -> bool:
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

    def kruskal(self, edges: Iterable[Tuple[int, int, int]]) -> int:
        """クラスカル法: 最小全域木 (Minimum spanning tree) の重みの総和"""
        return sum(w for u, v, w in edges if self.unite(u, v))


def sum_2d(table: Iterable[Iterable[int]]) -> int:
    return sum(map(sum, table))


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H - 1)]


def num(i: int, j: int) -> int:
    return i * W + j


print(
    sum_2d(A)
    + sum_2d(B)
    - UnionFind(H * W).kruskal(
        sorted(
            [
                (num(i, j), num(i, j + 1), A[i][j])
                for i in range(H)
                for j in range(W - 1)
            ]
            + [
                (num(i, j), num(i + 1, j), B[i][j])
                for i in range(H - 1)
                for j in range(W)
            ],
            key=itemgetter(2),
            reverse=True,
        )
    )
)
