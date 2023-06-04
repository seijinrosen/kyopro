X = int(input())


def solve() -> int:
    k = X

    while k % 360 != 0:
        k += X

    return k // X


print(solve())
