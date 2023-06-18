N, V, *A = map(int, open(0).read().split())


def solve() -> int:
    return A.count(V)


print(solve())
