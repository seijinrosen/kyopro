N, M, X, *A = map(int, open(0).read().split())


def solve() -> int:
    return min(sum(a <= X for a in A), sum(X <= a for a in A))


print(solve())
