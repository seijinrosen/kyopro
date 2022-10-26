N = int(input())
P = list(map(int, input().split()))

ans = sum(sorted([P[i - 1], P[i], P[i + 1]])[1] == P[i] for i in range(1, N - 1))
print(ans)
