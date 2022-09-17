N, K = map(int, input().split())
P = list(map(int, input().split()))

bucket = [False] * (N + 1)
for p in P[:K]:
    bucket[p] = True

idx = bucket.index(True)
ans_list = [idx]

for p in P[K:]:
    if idx < p:
        bucket[p] = True
        idx = bucket.index(True, idx + 1)
    ans_list.append(idx)

print(*ans_list, sep="\n")
