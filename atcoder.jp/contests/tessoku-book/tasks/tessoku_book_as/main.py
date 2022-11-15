from typing import Tuple


def input_nc() -> Tuple[int, str]:
    n, c = input().split()
    return int(n), c


N, C = input_nc()
A = input()

score_dict = {
    "W": 0,
    "B": 1,
    "R": 2,
}

score = sum(score_dict[c] for c in A)
ans = score % 3 == score_dict[C]

print("Yes" if ans else "No")
