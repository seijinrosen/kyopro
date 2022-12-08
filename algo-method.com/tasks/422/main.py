def f(x: int) -> int:
    if x == 0:
        return 0
    return f(x - 1) + x


print(f(int(input())))
