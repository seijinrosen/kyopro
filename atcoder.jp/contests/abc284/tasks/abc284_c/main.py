from typing import List, Tuple


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


N, M = map(int, input().split())
UV: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(M)]

uf = UnionFind(N)

for u, v in UV:
    u -= 1
    v -= 1
    uf.unite(u, v)

print(uf.group)
