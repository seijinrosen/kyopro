from functools import reduce
from math import gcd
from typing import Tuple

ABC: Tuple[int, int, int] = tuple(map(int, input().split()))

ans = sum(ABC) // reduce(gcd, ABC) - 3
print(ans)
