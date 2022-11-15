from typing import Tuple


def input_nc() -> Tuple[int, str]:
    n, c = input().split()
    return int(n), c


N, C = input_nc()
A = input()

score_list = "WBR"
ans = sum(map(score_list.index, A)) % 3 == score_list.index(C)

print("Yes" if ans else "No")
