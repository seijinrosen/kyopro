from math import gcd


def lcm(x: int, y: int) -> int:
    return x // gcd(x, y) * y


A, B = map(int, input().split())

ans = lcm(A, B)
print("Large" if 10**18 < ans else ans)
