def div_ceil(a: int, b: int) -> int:
    return (a + b - 1) // b


N = int(input())

ans = div_ceil(N, 111) * 111
print(ans)
