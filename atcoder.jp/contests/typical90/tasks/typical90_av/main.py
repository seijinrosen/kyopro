from typing import List, Tuple

N, K = map(int, input().split())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

ans = sum(sorted((x for a, b in AB for x in [b, a - b]), reverse=True)[:K])
print(ans)
