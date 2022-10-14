N, M = map(int, input().split())

ans = 0
new = N
old = 0

while new:
    ans += new
    old += new

    new = old // M
    old %= M

print(ans)
