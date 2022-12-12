def div_ceil(a: int, b: int) -> int:
    return (a + b - 1) // b


X, Y, Z = map(int, input().split())

ans = div_ceil(Y * Z, X) - 1
print(ans)
