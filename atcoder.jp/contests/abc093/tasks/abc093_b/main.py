from typing import List

A, B, K = map(int, input().split())


def solve() -> List[int]:
    return sorted(
        {*range(A, min(B, A + K)), *reversed(range(max(A, B - K + 1), B + 1))}
    )


print(*solve(), sep="\n")
