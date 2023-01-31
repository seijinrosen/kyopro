N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]


ans = sum(any(s.endswith(t) for t in T) for s in S)


print(ans)
