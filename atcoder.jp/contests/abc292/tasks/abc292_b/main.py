from typing import List, Tuple

N, Q = map(int, input().split())
events: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(Q)]


lst = [0] * N

for e, x in events:
    x -= 1

    if e == 1:
        lst[x] += 1
    elif e == 2:
        lst[x] += 2
    elif e == 3:
        print("Yes" if 2 <= lst[x] else "No")
