N, T = map(int, input().split())
T_LIST = list(map(int, input().split()))

ans = sum(min(T, T_LIST[i + 1] - T_LIST[i]) for i in range(N - 1)) + T
print(ans)
