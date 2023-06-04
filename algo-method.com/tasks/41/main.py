from typing import List, Tuple

N = int(input())
A: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(N)]


def solve() -> int:
    dp = [A[0]]

    for x, y, z in A[1:]:
        a, b, c = dp[-1]
        row = (x + max(b, c), y + max(a, c), z + max(a, b))
        dp.append(row)

    return max(dp[N - 1])


print(solve())
