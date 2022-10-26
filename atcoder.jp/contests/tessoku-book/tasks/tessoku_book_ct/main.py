from itertools import tee
from typing import Iterable, TypeVar

_T = TypeVar("_T")


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


N = int(input())
S = input()

# dp[l][r]: l 文字目から r 文字目までの部分における最長回文の長さ (0-indexed)
dp = [[int(i == j) for j in range(N)] for i in range(N)]

for i, (s, t) in enumerate(pairwise(S)):
    dp[i][i + 1] = 1 + (s == t)

# LEN = r - l
for LEN in range(2, N):
    for l in range(N - LEN):
        r = l + LEN
        dp[l][r] = max(
            dp[l][r - 1], dp[l + 1][r], dp[l + 1][r - 1] + 2 if S[l] == S[r] else 0
        )

ans = dp[0][N - 1]
print(ans)
