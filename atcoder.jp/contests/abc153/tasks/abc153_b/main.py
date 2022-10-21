from typing import Union


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


input_int_list = lambda: list(map(int, input().split()))


H, N = input_int_list()
A = input_int_list()

ans = H <= sum(A)
print(yes_no(ans))
