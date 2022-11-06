from math import factorial


def nCr(n: int, r: int) -> int:
    if n < r:
        return 0
    return factorial(n) // factorial(r) // factorial(n - r)


N, R = map(int, input().split())

ans = nCr(N, R) % 1000000007
print(ans)
