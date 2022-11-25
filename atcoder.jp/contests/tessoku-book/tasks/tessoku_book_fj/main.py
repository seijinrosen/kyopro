from typing import List, Tuple

N, M, K = map(int, input().split())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(M)]


# l ページ目から r ページ目までの間に、何個の繋がりがあるか
def score(l: int, r: int) -> int:
    return sum(l <= a and b <= r for a, b in AB)


# dp[i][j]: 現時点で i 章までの割り当てが決まっており、i 章の最後のページが j ページ目であることを考える
# この時点での小説の良さの最大値はいくつか
dp = [[-(10**6)] * (N + 1) for _ in range(K + 1)]
dp[0][0] = 0


for i in range(1, K + 1):
    for j in range(1, N + 1):
        # k: 前の章がどのページで終わったか
        for k in range(j):
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + score(k + 1, j))


ans = dp[K][N]
print(ans)
