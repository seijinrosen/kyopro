from itertools import combinations
from typing import Union


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


# input functions --------------------------------------------------------------
def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


N = int(input())
A = input_int_list()

ans = any(a + b + c == 1000 for a, b, c in combinations(A, 3))
print(yes_no(ans))
