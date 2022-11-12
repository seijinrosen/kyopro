from collections import defaultdict, deque
from typing import DefaultDict, List, Set, Tuple

N = int(input())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

G: DefaultDict[int, Set[int]] = defaultdict(set)
for a, b in AB:
    G[a].add(b)
    G[b].add(a)

visited = {1}
que = deque([1])

while que:
    v = que.popleft()
    for nv in G[v]:
        if nv not in visited:
            visited.add(nv)
            que.append(nv)

ans = max(visited)
print(ans)
