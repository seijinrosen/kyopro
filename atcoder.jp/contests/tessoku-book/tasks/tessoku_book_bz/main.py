from typing import Iterator


def input_ints() -> Iterator[int]:
    for i in map(int, input().split()):
        yield i


A, B = input_ints()

ans = A + B
print(ans)
