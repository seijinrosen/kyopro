from bisect import bisect
from functools import partial

input()
A = sorted(map(int, input().split()))
B = map(int, input().split())

ans = map(partial(bisect, A), B)
print(*ans, sep="\n")
