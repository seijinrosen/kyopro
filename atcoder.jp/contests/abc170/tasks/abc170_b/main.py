X, Y = map(int, input().split())

Z = 4 * X - Y
ans = any(2 * crane == Z for crane in range(X + 1))

print("Yes" if ans else "No")
