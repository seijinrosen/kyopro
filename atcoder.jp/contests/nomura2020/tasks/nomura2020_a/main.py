H1, M1, H2, M2, K = map(int, input().split())

x = 60 * H1 + M1
y = 60 * H2 + M2
if y < x:
    y += 60 * 24

ans = y - x - K
print(ans)
