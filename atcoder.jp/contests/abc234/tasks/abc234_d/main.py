N, K = map(int, input().split())
P = list(map(int, input().split()))

lst = [False] * (N + 1)
for p in P[:K]:
    lst[p] = True

i = min(P[:K])
ans_list = [i]

for p in P[K:]:
    if i < p:
        i += 1
        lst[p] = True
        while not lst[i]:
            i += 1
    ans_list.append(i)

print(*ans_list, sep="\n")
