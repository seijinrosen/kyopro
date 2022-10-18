from typing import List, Tuple

N, D = map(int, input().split())
XY: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

ans = sum(x**2 + y**2 <= D**2 for x, y in XY)
print(ans)
