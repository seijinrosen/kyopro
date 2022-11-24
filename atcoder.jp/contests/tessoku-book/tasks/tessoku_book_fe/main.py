from bisect import bisect_right
from functools import partial
from itertools import accumulate

N = int(input())
C = map(int, input().split())
Q = int(input())
X = (int(input()) for _ in range(Q))

acc = list(accumulate(sorted(C)))
ans = map(partial(bisect_right, acc), X)

print(*ans, sep="\n")
