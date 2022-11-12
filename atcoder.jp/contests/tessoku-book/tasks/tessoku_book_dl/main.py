from typing import List, Tuple

N, D = map(int, input().split())
XY: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

completed = [False] * N
ans = 0

for d in range(1, D + 1):
    max_i = -1
    max_y = 0

    for i, (x, y) in enumerate(XY):
        if all([not completed[i], x <= d, max_y < y]):
            max_i = i
            max_y = y

    if max_i != -1:
        completed[max_i] = True
        ans += max_y

print(ans)
