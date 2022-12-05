from bisect import bisect_left
from functools import partial

N, *A = map(int, open(0).read().split())

ans = map(partial(bisect_left, sorted(A)), A)
print(*ans, sep="\n")
