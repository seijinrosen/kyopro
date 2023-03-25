def div_ceil(a: int, b: int) -> int:
    return (a + b - 1) // b


N, *ABCDE = map(int, open(0).read().split())


ans = div_ceil(N, min(ABCDE)) + 4


print(ans)
