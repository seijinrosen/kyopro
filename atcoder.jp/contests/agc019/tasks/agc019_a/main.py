Q, H, S, D, N = map(int, open(0).read().split())


ans = 0
remaining = 4 * N

if D < 8 * Q and D < 4 * H and D < 2 * S:
    unit = remaining // 8
    ans += D * unit
    remaining -= 8 * unit

if S < 4 * Q and S < 2 * H:
    unit = remaining // 4
    ans += S * unit
    remaining -= 4 * unit

if H < 2 * Q:
    unit = remaining // 2
    ans += H * unit
    remaining -= 2 * unit

ans += Q * remaining


print(ans)
