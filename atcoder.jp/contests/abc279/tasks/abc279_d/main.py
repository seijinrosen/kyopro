A, B = map(int, input().split())

lo = 1
hi = 10**18
g = 1

for _ in range(100000):
    g = (lo + hi) // 2

    a = A / (g**0.5)
    b = A / ((g + 1) ** 0.5)

    if a - b > B:
        lo = g + 1
    else:
        hi = g

if g == 1:
    a = A / g**0.5 + B * (g - 1)
    c = A / (g + 1) ** 0.5 + B * g
    print(min(a, c))
else:
    a = A / g**0.5 + B * (g - 1)
    b = A / (g - 1) ** 0.5 + B * (g - 2)
    c = A / (g + 1) ** 0.5 + B * g
    print(min(a, b, c))
