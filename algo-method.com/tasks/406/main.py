N, K = map(int, input().split())

ans = sum(min(N, K // i) for i in range(1, N + 1))
print(ans)
