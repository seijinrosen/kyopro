N = int(input())
S = input()
K = int(input())

ans = "".join(c if c == S[K - 1] else "*" for c in S)
print(ans)
