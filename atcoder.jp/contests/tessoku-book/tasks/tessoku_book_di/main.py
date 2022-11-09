N, K = map(int, input().split())
S = input()

ans = S.count("1") % 2 == K % 2
print("Yes" if ans else "No")
