from math import atan2, cos, degrees, pi, sin, sqrt
from typing import Iterable


def dist(p: Iterable[float], q: Iterable[float]) -> float:
    # https://docs.python.org/ja/3/library/math.html#math.dist
    return sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))


T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = [int(input()) for _ in range(Q)]

r = L / 2
rad = 2 * pi / T

for e in E:
    angle = 3 * pi / 2 - e * rad
    y = r * cos(angle)
    z = r + r * sin(angle)
    d = dist((0, y), (X, Y))
    ans = atan2(z, d)
    print(degrees(ans))
