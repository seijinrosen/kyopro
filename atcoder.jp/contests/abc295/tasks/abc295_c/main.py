from collections import Counter

N, *A = map(int, open(0).read().split())


counter = Counter(A)
ans = sum(v // 2 for v in counter.values())


print(ans)
