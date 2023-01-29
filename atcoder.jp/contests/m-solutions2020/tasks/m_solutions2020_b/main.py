a, b, c, K = map(int, open(0).read().split())


for _ in range(K + 1):
    if a < b < c:
        print("Yes")
        exit()

    if a >= b:
        b *= 2
    elif b >= c:
        c *= 2


print("No")
