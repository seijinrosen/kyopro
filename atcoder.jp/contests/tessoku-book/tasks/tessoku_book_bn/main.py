from typing import List, Tuple


class UnionFind:
    # https://algo-method.com/descriptions/136
    def __init__(self, n: int) -> None:
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

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
        return True

    def size(self, x: int) -> int:
        return self.siz[self.root(x)]


N, Q = map(int, input().split())
TUV: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(Q)]

uf = UnionFind(N)

for t, u, v in TUV:
    if t == 1:
        uf.unite(u - 1, v - 1)
    elif t == 2:
        ans = uf.is_same(u - 1, v - 1)
        print("Yes" if ans else "No")
