import math
from functools import reduce
from typing import Set

N, *A = map(int, open(0).read().split())


gcd = reduce(math.gcd, A)
st: Set[int] = set()
ans = 0

for a in A:
    a //= gcd
    while a % 2 == 0:
        a //= 2
        ans += 1
    while a % 3 == 0:
        a //= 3
        ans += 1
    st.add(a)

ans = -1 if 1 < len(st) else ans


print(ans)
