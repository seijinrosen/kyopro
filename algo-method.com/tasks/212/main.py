N, *A = map(int, open(0).read().split())


def solve() -> int:
    return sum(0 < a for a in A)


print(solve())
