from collections import Counter
from itertools import product

input()
counters = (Counter(int(x) % 46 for x in input().split()).items() for _ in range(3))

ans = sum(
    x * y * z for (a, x), (b, y), (c, z) in product(*counters) if (a + b + c) % 46 == 0
)
print(ans)
