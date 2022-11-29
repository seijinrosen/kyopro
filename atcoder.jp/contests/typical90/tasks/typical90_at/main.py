from collections import Counter
from itertools import product

counters = (Counter(int(x) % 46 for x in row.split()).items() for row in [*open(0)][1:])

ans = sum(
    x * y * z for (a, x), (b, y), (c, z) in product(*counters) if (a + b + c) % 46 == 0
)
print(ans)
