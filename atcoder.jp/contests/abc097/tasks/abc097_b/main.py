X = int(input())


def solve() -> int:
    ans = 1

    for b in range(1, 1001):
        for p in range(2, 1001):
            if X < b**p:
                break

            ans = max(ans, b**p)

    return ans


print(solve())
