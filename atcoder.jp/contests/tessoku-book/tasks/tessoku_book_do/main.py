from itertools import product
from typing import List, Tuple

N = int(input())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

ans = max(
    sum(max(0, x * a + y * b) for a, b in AB) for x, y in product([-1, 1], repeat=2)
)

print(ans)
