from typing import List, Tuple

D, N = map(int, input().split())
LRH: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

working_hours = [0] + [24] * D

for l, r, h in LRH:
    for day in range(l, r + 1):
        working_hours[day] = min(working_hours[day], h)

ans = sum(working_hours)
print(ans)
