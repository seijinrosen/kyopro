from typing import List, Tuple

N, T = map(int, input().split())
CT: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]


ans = min((c for c, t in CT if t <= T), default="TLE")


print(ans)
