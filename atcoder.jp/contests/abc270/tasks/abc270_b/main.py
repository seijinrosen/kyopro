X, Y, Z = map(int, input().split())

if 0 < X and Y < 0:
    print(X)
    exit()

if X < 0 and 0 < Y:
    print(abs(X))
    exit()

if 0 < X and X < Y:
    print(X)
    exit()

if X < 0 and Y < X:
    print(abs(X))
    exit()

if 0 < Y and Y < Z:
    print(-1)
    exit()

if Y < 0 and Z < Y:
    print(-1)
    exit()

ans = abs(Z) + abs(X - Z)
print(ans)
