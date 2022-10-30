from functools import partial


def div_ceil(a: int, b: int) -> int:
    return (a + b - 1) // b


N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = X + sum(map(partial(div_ceil, D), A))
print(ans)
