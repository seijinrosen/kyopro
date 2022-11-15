from collections import Counter

N, M = map(int, input().split())
A = map(int, input().split())

counter = Counter(A)
ans = [M - counter[i] for i in range(1, N + 1)]

print(*ans, sep="\n")
