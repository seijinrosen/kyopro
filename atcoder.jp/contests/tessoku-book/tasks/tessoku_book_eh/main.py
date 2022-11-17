from collections import Counter
from itertools import chain
from typing import List, Tuple

N, M = map(int, input().split())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(M)]

counter = Counter(chain.from_iterable(AB))
ans = counter.most_common(1)[0][0]

print(ans)
