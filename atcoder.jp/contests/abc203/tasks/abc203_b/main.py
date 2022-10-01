N, K = map(int, input().split())

ans = sum(100 * i + j for i in range(1, N + 1) for j in range(1, K + 1))
print(ans)
