from itertools import combinations
from operator import itemgetter
from typing import Iterable, List, Tuple


class UnionFind:
    # https://algo-method.com/descriptions/136
    def __init__(self, n: int) -> None:
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n
        self.group = n

    def root(self, x: int) -> int:
        if self.par[x] == -1:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

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
        self.siz[rx] += self.siz[ry]
        self.group -= 1
        return True

    def size(self, x: int) -> int:
        return self.siz[self.root(x)]

    def kruskal(
        self, edges: Iterable[Tuple[int, int, int]], already_sorted: bool = False
    ) -> int:
        """クラスカル法: 最小全域木 (Minimum spanning tree) の重みの総和"""
        if not already_sorted:
            edges = sorted(edges, key=itemgetter(2))
        return sum(w for u, v, w in edges if self.unite(u, v))


N, M = map(int, input().split())
UVW: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(M)]

UVW.sort(key=itemgetter(2))
W = UnionFind(N).kruskal(UVW, True)

ans = 0
for edges in combinations(UVW, M - 1):
    uf = UnionFind(N)
    w = uf.kruskal(edges, True)
    if 1 < uf.group or W < w:
        ans += 1

print(ans)
