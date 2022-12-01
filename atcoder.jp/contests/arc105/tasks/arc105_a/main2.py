ABCD = map(int, input().split())

A, B, C, D = sorted(ABCD)
ans = A + B + C == D or A + D == B + C

print("Yes" if ans else "No")
