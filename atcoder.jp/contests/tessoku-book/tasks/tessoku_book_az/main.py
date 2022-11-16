from collections import deque
from typing import Deque

Q = int(input())
QUERIES = [input().split() for _ in range(Q)]

que: Deque[str] = deque()

for query in QUERIES:
    q = int(query[0])

    if q == 1:
        x = query[1]
        que.append(x)

    elif q == 2:
        print(que[0])

    elif q == 3:
        que.popleft()
