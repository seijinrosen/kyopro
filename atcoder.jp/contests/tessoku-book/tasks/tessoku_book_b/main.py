from typing import Iterator, Union


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


def input_ints() -> Iterator[int]:
    for i in map(int, input().split()):
        yield i


def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


N, X = input_ints()
A = input_int_list()

ans = X in A
print(yes_no(ans))
