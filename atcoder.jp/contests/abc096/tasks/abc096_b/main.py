A, B, C, K = map(int, open(0).read().split())


lst = sorted([A, B, C])
for _ in range(K):
    lst[-1] *= 2

ans = sum(lst)


print(ans)
