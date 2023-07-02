x, y, k = map(int, open(0).read().split())


def solve() -> int:
    if k <= y:
        return x + k

    z = k - y
    return x - z + y


print(solve())
