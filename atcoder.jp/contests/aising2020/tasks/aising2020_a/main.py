L, R, D = map(int, input().split())

ans = R // D - (L - 1) // D
print(ans)
