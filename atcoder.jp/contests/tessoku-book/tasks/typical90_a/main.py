N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def check(score: int) -> bool:
    cnt = 0
    now = 0
    for a in A:
        if score <= a - now:
            cnt += 1
            now = a
        if cnt == K:
            return score <= L - now
    return False


lo = 1
hi = L
while hi - lo > 1:
    mid = (lo + hi) // 2
    if check(mid):
        lo = mid
    else:
        hi = mid

ans = lo
print(ans)
