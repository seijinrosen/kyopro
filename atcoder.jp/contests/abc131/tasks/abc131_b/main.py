N, L = map(int, input().split())


def solve() -> int:
    first = L
    last = L + N - 1
    total = (first + last) * N // 2

    if last < 0:
        return total - last

    if 0 < first:
        return total - first

    return total


print(solve())
