N = int(input())


def solve() -> int:
    return min(range(0, 101, 5), key=lambda i: abs(i - N))


print(solve())
