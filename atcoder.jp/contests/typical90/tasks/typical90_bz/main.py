from typing import List, Tuple

N, M = map(int, input().split())
AB: List[Tuple[int, int]] = [
    tuple(int(x) - 1 for x in input().split()) for _ in range(M)
]

G: List[List[int]] = [[] for _ in range(N)]
for a, b in AB:
    G[a].append(b)
    G[b].append(a)

ans = sum(sum(j < i for j in g) == 1 for i, g in enumerate(G))
print(ans)
