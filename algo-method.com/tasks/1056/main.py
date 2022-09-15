N, X = map(int, input().split())

ans = "Yes" if N & 1 << X else "No"
print(ans)
