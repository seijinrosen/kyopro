N = int(input())
S = input()

ans = S[: N // 2] == S[N // 2 :]
print("Yes" if ans else "No")
