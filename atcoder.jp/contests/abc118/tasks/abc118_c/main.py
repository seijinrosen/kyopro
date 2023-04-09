import math
from functools import reduce

N, *A = map(int, open(0).read().split())


ans = reduce(math.gcd, A)


print(ans)
