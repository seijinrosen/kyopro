N = input()


def solve() -> int:
    k = len(N)

    if k == 1:
        return int(N)

    if all(x == "9" for x in N[1:]):
        return int(N[0]) + 9 * (k - 1)

    return int(N[0]) + 9 * (k - 1) - 1


print(solve())
