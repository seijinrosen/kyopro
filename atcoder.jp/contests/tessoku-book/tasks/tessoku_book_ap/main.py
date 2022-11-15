from typing import List, Tuple

N, K = map(int, input().split())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

ans = max(
    sum(min_a <= a <= min_a + K and min_b <= b <= min_b + K for a, b in AB)
    for min_a in range(1, 101)
    for min_b in range(1, 101)
)

print(ans)
