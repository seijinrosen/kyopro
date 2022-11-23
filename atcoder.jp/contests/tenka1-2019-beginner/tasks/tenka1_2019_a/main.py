A, B, C = map(int, input().split())

ans = A < C < B or B < C < A
print("Yes" if ans else "No")
