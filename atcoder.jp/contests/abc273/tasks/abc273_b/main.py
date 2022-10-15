from decimal import ROUND_HALF_UP, Decimal

X, K = map(int, input().split())

now = Decimal(X)
for i in range(1, K + 1):
    now = now.quantize(Decimal(f"1e{i}"), rounding=ROUND_HALF_UP)

ans = int(now)
print(ans)
