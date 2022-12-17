from itertools import combinations

N, M = map(int, input().split())
S = [[c == "o" for c in input()] for _ in range(N)]

ans = sum(all(map(any, zip(*comb))) for comb in combinations(S, 2))
print(ans)
