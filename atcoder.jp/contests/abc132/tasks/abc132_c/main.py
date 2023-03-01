from bisect import bisect_left

N, *D = map(int, open(0).read().split())


D.sort()

ans = 0
for k in range(1, max(D) + 1):
    abc = bisect_left(D, k)
    arc = N - abc
    if abc == arc:
        ans += 1


print(ans)
