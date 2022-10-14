R, D, X2000 = map(int, input().split())

x = X2000

for _ in range(10):
    x = R * x - D
    print(x)
