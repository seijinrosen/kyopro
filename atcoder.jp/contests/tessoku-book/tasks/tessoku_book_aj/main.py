N, K = map(int, input().split())

ans = (N - 1) * 2 <= K and K % 2 == 0
print("Yes" if ans else "No")
