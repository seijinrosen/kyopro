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


# https://atcoder.jp/contests/abc279/editorial/5284
N, Q = map(int, input().split())
OP = [map(int, input().split()) for _ in range(Q)]

uf = UnionFind(N + Q + 5)
balls = N

# ld[x]: 箱 x に入っている集合の代表元
# 但し、箱 x が空である場合は -1 とする
ld = [-1] * (N + 1)

# inv[y]: 代表元が y である集合がどの箱に入っているか
# 但し、代表元が y である集合がない場合の値は不定である
inv = [0] * (N + Q + 5)

for i in range(1, N + 1):
    ld[i] = i
    inv[ld[i]] = i

for t, x, *q in OP:
    if t == 1:
        y = q[0]
        if ld[y] == -1:
            continue
        if ld[x] == -1:
            ld[x] = ld[y]
        else:
            uf.unite(ld[x], ld[y])
            ld[x] = uf.root(ld[x])
        inv[ld[x]] = x
        ld[y] = -1

    elif t == 2:
        balls += 1
        if ld[x] == -1:
            ld[x] = balls
        else:
            uf.unite(ld[x], balls)
            ld[x] = uf.root(balls)
        inv[ld[x]] = x

    elif t == 3:
        ans = inv[uf.root(x)]
        print(ans)
