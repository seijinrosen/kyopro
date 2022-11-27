def div_ceil(a: int, b: int) -> int:
    return (a + b - 1) // b


H, W = map(int, input().split())

if 1 in {H, W}:
    ans = H * W
else:
    ans = div_ceil(W, 2) * div_ceil(H, 2)

print(ans)
