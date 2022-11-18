from collections import deque
from typing import List, Tuple

N, M = map(int, input().split())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(M)]

G: List[List[int]] = [[] for _ in range(N)]
for a, b in AB:
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

ans = [-1] * N
ans[0] = 0

que = deque([0])
while que:
    v = que.popleft()
    for nv in G[v]:
        if ans[nv] == -1:
            ans[nv] = ans[v] + 1
            que.append(nv)

print(*ans, sep="\n")
