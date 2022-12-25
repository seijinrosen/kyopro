# 参考: https://atcoder.jp/contests/abc283/submissions/37526455


from typing import List

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

INF = 10**9


def flip(lst: List[int]) -> List[int]:
    return [1 - a for a in lst]


def is_ok(lst0: List[int], lst1: List[int], lst2: List[int]) -> bool:
    for j in range(W):
        candidates = {lst0[j], lst2[j]}
        if 0 < j:
            candidates.add(lst1[j - 1])
        if j < W - 1:
            candidates.add(lst1[j + 1])
        if lst1[j] not in candidates:
            return False
    return True


dp = [INF] * 4
for s in range(4):
    lst0 = [-1] * W
    lst1 = flip(A[0]) if s & 2 else A[0]
    lst2 = flip(A[1]) if s & 1 else A[1]
    if is_ok(lst0, lst1, lst2):
        dp[s] = bool(s & 1) + bool(s & 2)


for i in range(2, H):
    now = [INF] * 4
    for s in range(4):
        lst0 = flip(A[i - 2]) if s & 2 else A[i - 2]
        lst1 = flip(A[i - 1]) if s & 1 else A[i - 1]
        for x in range(2):
            lst2 = flip(A[i]) if x else A[i]
            if is_ok(lst0, lst1, lst2):
                ns = (s & 1) << 1 | x
                now[ns] = min(now[ns], dp[s] + x)
    dp = now


ans = INF
for s in range(4):
    lst0 = flip(A[-2]) if s & 2 else A[-2]
    lst1 = flip(A[-1]) if s & 1 else A[-1]
    lst2 = [-1] * W
    if is_ok(lst0, lst1, lst2):
        ans = min(ans, dp[s])


print(-1 if ans == INF else ans)
