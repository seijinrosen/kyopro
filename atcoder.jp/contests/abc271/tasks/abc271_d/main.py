N, S = map(int, input().split())
AB: "list[tuple[int, int]]" = [tuple(map(int, input().split())) for _ in range(N)]

dp = [["x"] * (S + 1) for _ in range(N + 1)]
dp[0][0] = ""

for i in range(N):
    for j in range(S + 1):
        if dp[i][j] == "x":
            continue

        a, b = AB[i]

        if j + AB[i][0] <= S:
            dp[i + 1][j + a] = dp[i][j] + "H"

        if j + AB[i][1] <= S:
            dp[i + 1][j + b] = dp[i][j] + "T"

if dp[N][S] == "x":
    print("No")
    exit()

ans = dp[N][S]
print("Yes")
print(ans)
