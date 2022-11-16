from heapq import heappop, heappush
from typing import List

N, D = map(int, input().split())

G: List[List[int]] = [[] for _ in range(D)]
for _ in range(N):
    x, y = map(int, input().split())
    G[x - 1].append(y)


heap: List[int] = []
ans = 0

for g in G:
    for y in g:
        heappush(heap, -y)
    if heap:
        ans -= heappop(heap)

print(ans)
