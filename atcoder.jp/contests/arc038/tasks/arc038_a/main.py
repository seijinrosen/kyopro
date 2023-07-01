N, *A = map(int, open(0).read().split())


def solve() -> int:
    return sum(sorted(A, reverse=True)[::2])


print(solve())
