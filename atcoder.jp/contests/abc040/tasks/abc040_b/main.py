from math import inf

n = int(input())


ans = inf
for x in range(1, n + 1):
    y = n // x
    ans = min(ans, abs(x - y) + n - x * y)


print(ans)
