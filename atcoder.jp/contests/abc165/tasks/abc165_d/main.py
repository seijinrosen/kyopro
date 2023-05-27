A, B, N = map(int, input().split())


def func(x: int) -> int:
    return (A * x) // B - A * (x // B)


def solve() -> int:
    return func(min(B - 1, N))


print(solve())
