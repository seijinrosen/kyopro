from collections import Counter

N, M, *A = map(int, open(0).read().split())

counter = Counter(a % M for a in A)
ans = sum(counter[r] * (counter[r] - 1) // 2 for r in range(M))

print(ans)
