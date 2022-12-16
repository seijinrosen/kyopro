from typing import List, Tuple

N, H, W = map(int, input().split())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

ans = sum(H <= a and W <= b for a, b in AB)
print(ans)
