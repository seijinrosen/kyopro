from bisect import bisect_left
from functools import partial

input()
A = list(map(int, input().split()))
B = map(int, input().split())

ans = map(partial(bisect_left, A), B)
print(*ans, sep="\n")
