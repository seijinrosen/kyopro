from itertools import accumulate
from typing import List, Tuple

Pair = Tuple[int, int]


def input_int_pair_list(n: int) -> List[Pair]:
    return [tuple(map(int, input().split())) for _ in range(n)]


N = int(input())
A = list(map(int, input().split()))
D = int(input())
LR = input_int_pair_list(D)

left_acc = [*accumulate(A, max)]
right_acc = [*accumulate(A[::-1], max)][::-1]

ans = [max(left_acc[l - 2], right_acc[r]) for l, r in LR]
print(*ans, sep="\n")
