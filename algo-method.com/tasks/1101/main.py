from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

ans = accumulate(A, max)
print(*ans, sep="\n")
