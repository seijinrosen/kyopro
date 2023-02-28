N, *X = map(int, open(0).read().split())


X.sort()
ans = sum(X[N:-N]) / (3 * N)


print(ans)
