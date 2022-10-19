from typing import List, Tuple

input_int_list = lambda: list(map(int, input().split()))


def input_int_tuple_list(n: int) -> List[Tuple[int, int]]:
    return [tuple(map(int, input().split())) for _ in range(n)]


N, W = input_int_list()
WV = input_int_tuple_list(N)

dp = [[0] * (W + 1)]
for w, v in WV:
    dp += [[max(dp[-1][j], dp[-1][j - w] + v if w <= j else 0) for j in range(W + 1)]]

ans = dp[N][W]
print(ans)
