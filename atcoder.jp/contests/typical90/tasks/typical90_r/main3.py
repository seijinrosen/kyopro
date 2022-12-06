from math import atan2, cos, degrees, dist, pi, sin

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = [int(input()) for _ in range(Q)]

r = L / 2

for e in E:
    angle = 2 * pi * e / T
    y = -r * sin(angle)
    z = -r * cos(angle) + r
    d = dist((0, y), (X, Y))
    ans = atan2(z, d)
    print(degrees(ans))
