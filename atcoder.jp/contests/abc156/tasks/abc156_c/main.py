N, *X = map(int, open(0).read().split())


ans = min(sum((x - p) ** 2 for x in X) for p in range(min(X), max(X) + 1))


print(ans)
