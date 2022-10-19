from typing import List, Tuple

input_int_list = lambda: list(map(int, input().split()))


def input_int_tuple_list(n: int) -> List[Tuple[int, int]]:
    return [tuple(map(int, input().split())) for _ in range(n)]


N, W = input_int_list()
WV = input_int_tuple_list(N)

max_V = sum(v for _, v in WV)
dp = [[0] + [W + 1] * max_V]

for w, v in WV:
    dp += [
        [
            min(dp[-1][j], dp[-1][j - v] + w if v <= j else W + 1)
            for j in range(max_V + 1)
        ]
    ]

ans = next(j for j, w in reversed(list(enumerate(dp[N]))) if w <= W)
print(ans)
