N = int(input())
S = input()

ans = sum(N**i * int(c) for i, c in enumerate(reversed(S)))
print(ans)
