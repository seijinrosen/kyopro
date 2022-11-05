from math import gcd


def lcm(x: int, y: int) -> int:
    """最小公倍数 (least common multiple)"""
    return x // gcd(x, y) * y


A, B = map(int, input().split())

ans = lcm(A, B)
print(ans)
