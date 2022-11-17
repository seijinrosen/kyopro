from typing import List, Tuple

N, M = map(int, input().split())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(M)]

G: List[List[int]] = [[] for _ in range(N + 1)]
for a, b in AB:
    G[a].append(b)
    G[b].append(a)

for k, g in enumerate(G[1:], start=1):
    print(k, end=": {")
    print(*sorted(g), sep=", ", end="}\n")
