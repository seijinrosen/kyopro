N, K = map(int, input().split())
S = [input() for _ in range(N)]


ans = sorted(S[:K])


print(*ans, sep="\n")
