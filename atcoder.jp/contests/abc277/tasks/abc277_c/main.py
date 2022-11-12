from collections import defaultdict, deque
from typing import List, Tuple

N = int(input())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

dic: "defaultdict[int, set[int]]" = defaultdict(set)
for a, b in AB:
    dic[a].add(b)
    dic[b].add(a)

visited = {1}
que = deque([1])

while que:
    nex = que.popleft()
    for nn in dic[nex]:
        if nn not in visited:
            que.append(nn)
            visited.add(nn)

ans = max(visited)
print(ans)
