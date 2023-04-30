N, K, *H = map(int, open(0).read().split())


H.sort()
ans = min(H[i + K - 1] - H[i] for i in range(N - K + 1))


print(ans)
