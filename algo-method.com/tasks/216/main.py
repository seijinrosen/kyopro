N, V, *A = map(int, open(0).read().split())


def solve() -> int:
    ans = -1

    for i, a in enumerate(A):
        if a == V:
            ans = i

    return ans


print(solve())
