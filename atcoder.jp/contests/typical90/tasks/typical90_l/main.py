from typing import Iterator, Tuple


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
        return True


def neighborhood(i: int, j: int, h: int, w: int) -> Iterator[Tuple[int, int]]:
    x = (-1, 0, 0, 1)
    y = (0, -1, 1, 0)
    for di, dj in zip(x, y):
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w:
            yield ni, nj


H, W = map(int, input().split())
Q = int(input())
QUERIES = [[int(x) - 1 for x in input().split()] for _ in range(Q)]

grid = [[False] * W for _ in range(H)]
uf = UnionFind(H * W)


def calc(r: int, c: int) -> int:
    return r * W + c


for q in map(iter, QUERIES):
    t = next(q)

    if t == 0:
        r, c = q
        grid[r][c] = True
        for nr, nc in neighborhood(r, c, H, W):
            if grid[nr][nc]:
                uf.unite(calc(r, c), calc(nr, nc))

    elif t == 1:
        ra, ca, rb, cb = q
        ans = "Yes" if grid[ra][ca] and uf.is_same(calc(ra, ca), calc(rb, cb)) else "No"
        print(ans)
