N, *A = map(int, open(0).read().split())


def solve() -> int:
    return A.index(max(A))


print(solve())
