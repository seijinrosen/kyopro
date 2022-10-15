N = int(input())


def f(x: int) -> int:
    if x == 0:
        return 1
    return x * f(x - 1)


print(f(N))
