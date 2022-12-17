from itertools import combinations

N, M = map(int, input().split())
S = [input() for _ in range(N)]

cnt = 0

for comb in combinations(range(N), 2):
    a, b = comb
    ans = True
    for j in range(M):
        if S[a][j] == "o" or S[b][j] == "o":
            continue
        ans = False
    if ans:
        cnt += 1

print(cnt)
