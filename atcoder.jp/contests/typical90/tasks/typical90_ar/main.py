from collections import deque
from typing import List, Tuple

N, Q = map(int, input().split())
A = deque(map(int, input().split()))
TXY: List[Tuple[int, int, int]] = [
    tuple(int(x) - 1 for x in input().split()) for _ in range(Q)
]

for t, x, y in TXY:
    if t == 0:
        A[x], A[y] = A[y], A[x]
    elif t == 1:
        A.rotate()
    elif t == 2:
        print(A[x])
