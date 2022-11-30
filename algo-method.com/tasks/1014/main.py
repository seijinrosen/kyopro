from operator import itemgetter
from typing import List, Tuple


class UnionFind:
    # https://algo-method.com/descriptions/136
    def __init__(self, n: int) -> None:
        self.par = [-1] * n
        self.rank = [0] * n
        self.group = n

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
        self.group -= 1
        return True


N, M = map(int, input().split())
UVW: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(M)]

UVW.sort(key=itemgetter(2))
uf = UnionFind(N)
mst_edge_nums = [i for i, (u, v, _) in enumerate(UVW) if uf.unite(u, v)]
W = sum(UVW[i][2] for i in mst_edge_nums)

ans = 0
for i in mst_edge_nums:
    uf = UnionFind(N)
    w = sum(w for j, (u, v, w) in enumerate(UVW) if i != j if uf.unite(u, v))
    if W < w or 1 < uf.group:
        ans += 1

print(ans)
