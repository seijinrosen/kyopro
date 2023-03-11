N, *A = map(int, open(0).read().split())


s = 0
for a in [0, *A]:
    s *= 2
    s += a


print(s)
