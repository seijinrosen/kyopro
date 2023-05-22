import math
from typing import List, Tuple

N = int(input())
ab: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]


ans = math.floor(sum(a * b for a, b in ab) * 1.05)


print(ans)
