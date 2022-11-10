from operator import itemgetter
from typing import List, Tuple

N = int(input())
LR: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

now = 0
ans = 0

for l, r in sorted(LR, key=itemgetter(1)):
    if now <= l:
        now = r
        ans += 1

print(ans)
