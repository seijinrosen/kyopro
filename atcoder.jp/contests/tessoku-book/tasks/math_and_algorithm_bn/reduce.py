from functools import reduce
from typing import List, Tuple

N = int(input())
LR: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]


def func(now_and_ans: Tuple[int, int], lr: Tuple[int, int]) -> Tuple[int, int]:
    now, ans = now_and_ans
    l, r = lr
    if now <= l:
        return r, ans + 1
    return now_and_ans


ans = reduce(func, sorted(LR, key=lambda t: t[1]), (0, 0))
print(ans[1])
