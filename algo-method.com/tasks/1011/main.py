from operator import itemgetter
from typing import List, Tuple


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


N, M = map(int, input().split())
UVW: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(M)]

uf = UnionFind(N)
ans = sum(w for u, v, w in sorted(UVW, key=itemgetter(2)) if uf.unite(u, v))

print(ans)
