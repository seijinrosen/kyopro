N, *P = map(int, open(0).read().split())


def solve() -> int:
    ans = 0

    for i in range(N - 1):
        if P[i] == i + 1:
            P[i], P[i + 1] = P[i + 1], P[i]
            ans += 1

    for i in reversed(range(1, N)):
        if P[i] == i + 1:
            P[i - 1], P[i] = P[i], P[i - 1]
            ans += 1

    return ans


print(solve())
