from itertools import product
from typing import List, Tuple

N = int(input())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]


ans = 10**9
for i, j in product(range(N), repeat=2):
    a = AB[i][0]
    b = AB[j][1]
    ans = min(ans, a + b if i == j else max(a, b))


print(ans)
