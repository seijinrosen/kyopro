from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

counter = Counter(S)
results = ["AC", "WA", "TLE", "RE"]

for r in results:
    print(r, "x", counter[r])
