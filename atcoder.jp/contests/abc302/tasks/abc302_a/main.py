def div_ceil(a: int, b: int) -> int:
    return (a + b - 1) // b


A, B = map(int, input().split())


ans = div_ceil(A, B)


print(ans)
