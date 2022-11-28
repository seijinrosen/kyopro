a, b, c = map(int, input().split())

ans = a < c**b
print("Yes" if ans else "No")
