from typing import List

N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[True] + [False] * S]
for a in A:
    dp += [[dp[-1][j] or (a <= j and dp[-1][j - a]) for j in range(S + 1)]]

if not dp[N][S]:
    print(-1)
    exit()

j = S
cards: List[int] = []

for i, a in reversed(list(enumerate(A, start=1))):
    if not dp[i - 1][j]:
        cards.append(i)
        j -= a

print(len(cards))
print(*cards[::-1])
