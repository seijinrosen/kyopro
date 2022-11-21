from collections import deque
from functools import partial, reduce
from itertools import compress
from operator import lshift, xor
from typing import List, Tuple

N, M = map(int, input().split())
A = map(int, input().split())
XYZ: List[Tuple[int, int, int]] = [
    tuple(int(x) - 1 for x in input().split()) for _ in range(M)
]

# start = sum(1 << i for i, a in enumerate(A) if a)
start = sum(1 << i for i in compress(range(N), A))
goal = (1 << N) - 1

dist = [-1] * (1 << N)
dist[start] = 0

que = deque([start])
while que:
    v = que.popleft()
    for xyz in XYZ:
        nv = reduce(xor, map(partial(lshift, 1), xyz), v)
        if dist[nv] == -1:
            dist[nv] = dist[v] + 1
            que.append(nv)

ans = dist[goal]
print(ans)
