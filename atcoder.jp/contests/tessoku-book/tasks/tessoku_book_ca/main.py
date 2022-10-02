from typing import Union


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


A, B = input_int_list()

ans = any(100 % i == 0 for i in range(A, B + 1))
print(yes_no(ans))
