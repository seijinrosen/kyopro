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


N, M = map(int, input().split())
AB: List[Tuple[int, int]] = [
    tuple(int(x) - 1 for x in input().split()) for _ in range(M)
]
Q = int(input())
QUERIES = [tuple(int(x) - 1 for x in input().split()) for _ in range(Q)]

uf = UnionFind(N)
for x in set(range(M)) - {q[1] for q in QUERIES if q[0] == 0}:
    uf.unite(*AB[x])

ans: List[str] = []
for q in map(iter, reversed(QUERIES)):
    t = next(q)
    if t == 0:
        uf.unite(*AB[next(q)])
    elif t == 1:
        ans.append("Yes" if uf.is_same(*q) else "No")

print(*reversed(ans), sep="\n")
