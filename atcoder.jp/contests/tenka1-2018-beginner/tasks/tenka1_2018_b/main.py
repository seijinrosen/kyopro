from typing import Tuple

a, b, K = map(int, input().split())


def func(x: int, y: int) -> Tuple[int, int]:
    if x % 2 == 1:
        x -= 1
    tmp = x // 2
    x -= tmp
    y += tmp
    return x, y


for i in range(K):
    if i % 2 == 0:
        a, b = func(a, b)
    else:
        b, a = func(b, a)


print(a, b)
