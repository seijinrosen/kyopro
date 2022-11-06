from math import factorial


def nCr(n: int, r: int, mod: int = 0) -> int:
    """組み合わせの数
    >>> nCr(4, 2)
    6
    """
    if n < r:
        return 0
    a = factorial(n)
    b = factorial(r) * factorial(n - r)
    if mod == 0:
        return a // b
    return a * pow(b, mod - 2, mod) % mod


H, W = map(int, input().split())

ans = nCr(H + W - 2, H - 1, 1000000007)
print(ans)
