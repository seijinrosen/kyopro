def div_ceil(a: int, b: int) -> int:
    return (a + b - 1) // b


N, D = map(int, input().split())

ans = div_ceil(N, 2 * D + 1)
print(ans)
