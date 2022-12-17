from itertools import combinations

N, M = map(int, input().split())
S = [[c == "o" for c in input()] for _ in range(N)]

ans = sum(all(x[j] or y[j] for j in range(M)) for x, y in combinations(S, 2))
print(ans)
