N, H, W = map(int, open(0).read().split())

h = N - H + 1
w = N - W + 1

print(h * w)
