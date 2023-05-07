N, A, B = map(int, input().split())


def solve() -> int:
    if A % 2 == B % 2:
        return (B - A) // 2
    return min(A - 1, N - B) + 1 + (B - A - 1) // 2


print(solve())
