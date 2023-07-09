N = int(input())


def solve() -> int:
    zero = 1
    one = 0
    two = 0

    for _ in range(N):
        two += one
        one = zero
        zero = two

    return zero + one + two


print(solve())
