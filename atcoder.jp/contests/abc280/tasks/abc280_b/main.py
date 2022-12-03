N = int(input())
S = list(map(int, input().split()))

ans = [S[0]]
now = S[0]

for s in S[1:]:
    ans.append(s - sum(ans))

print(*ans)
