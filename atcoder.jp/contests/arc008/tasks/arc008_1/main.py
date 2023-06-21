N = int(input())


def solve() -> int:
    x = N // 10
    return 100 * x + min(100, 15 * (N % 10))


print(solve())
