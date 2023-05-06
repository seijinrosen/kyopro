A, B = map(int, input().split())


def solve() -> int:
    ans = 0
    a, b = max(A, B), min(A, B)

    while 0 < b:
        ans += a // b
        a %= b
        a, b = b, a

    return ans - 1


print(solve())
