N, *A = map(int, open(0).read().split())


def solve() -> int:
    return sum(A[i] > A[i - 1] for i in range(1, N))


print(solve())
