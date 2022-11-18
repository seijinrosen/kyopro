def div_ceil(a: int, b: int) -> int:
    return (a + b - 1) // b


H = int(input())
W = int(input())
N = int(input())

ans = div_ceil(N, max(H, W))
print(ans)
