from typing import List, Tuple

A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
xyc: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(M)]


ans = min(min(a) + min(b), min(a[x - 1] + b[y - 1] - c for x, y, c in xyc))


print(ans)
