from typing import List

N, *A = map(int, open(0).read().split())


def solve() -> List[int]:
    ans = [0] * 9

    for a in A:
        ans[a - 1] += 1

    return ans


print(*solve(), sep="\n")
