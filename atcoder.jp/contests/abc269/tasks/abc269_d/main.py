import sys

sys.setrecursionlimit(10**9)

N = int(input())
XY: "list[tuple[int, int]]" = [tuple(map(int, input().split())) for _ in range(N)]

G = [[False] * 3000 for _ in range(3000)]
for x, y in XY:
    G[x][y] = True

DX = [-1, -1, 0, 0, 1, 1]
DY = [-1, 0, -1, 1, 0, 1]


def dfs(x: int, y: int) -> None:
    G[x][y] = False

    for dx, dy in zip(DX, DY):
        nx = x + dx
        ny = y + dy
        if G[nx][ny]:
            dfs(nx, ny)


ans = 0

for x, y in XY:
    if G[x][y]:
        dfs(x, y)
        ans += 1

print(ans)
