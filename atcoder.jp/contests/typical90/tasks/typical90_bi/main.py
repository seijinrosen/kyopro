from collections import deque
from typing import Deque, List, Tuple

Q = int(input())
TX: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(Q)]

que: Deque[int] = deque()

for t, x in TX:
    if t == 1:
        que.appendleft(x)
    elif t == 2:
        que.append(x)
    elif t == 3:
        print(que[x - 1])
