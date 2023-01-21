from typing import List, Tuple

N, X = map(int, input().split())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[False] * (X + 1)]
dp[0][0] = True

for a, b in AB:
    lst = [False] * (X + 1)
    for i in range(X + 1):
        if dp[-1][i]:
            for j in range(b + 1):
                if i + a * j < X + 1:
                    lst[i + a * j] = True
    dp.append(lst)

ans = dp[-1][-1]
print("Yes" if ans else "No")
