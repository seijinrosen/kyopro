from typing import List, Tuple

N = int(input())
PA: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

P = [0, *(p for p, _ in PA), 0]
A = [0, *(a for _, a in PA), 0]

# dp[l][r]: l 番目から r 番目までのブロックが残っているときの最大合計得点
dp = [[0] * (N + 2) for _ in range(N + 1)]

# LEN = r - l
for LEN in reversed(range(N - 1)):
    for l in range(1, N - LEN + 1):
        r = l + LEN
        score1 = A[l - 1] if l <= P[l - 1] <= r else 0
        score2 = A[r + 1] if l <= P[r + 1] <= r else 0
        dp[l][r] = max(dp[l - 1][r] + score1, dp[l][r + 1] + score2)

ans = max(dp[i][i] for i in range(1, N + 1))
print(ans)
