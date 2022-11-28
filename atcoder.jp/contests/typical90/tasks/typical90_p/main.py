N, A, B, C = map(int, open(0).read().split())

MAX_COIN_NUM = 10000
ans = N

for a in range(MAX_COIN_NUM):
    for b in range(MAX_COIN_NUM - a):
        cc = N - A * a - B * b
        c = max(0, cc // C)
        if C * c == cc:
            ans = min(ans, a + b + c)

print(ans)
