def div_ceil(a: int, b: int) -> int:
    return (a + b - 1) // b


N, K = map(int, input().split())


ans = K <= div_ceil(N, 2)


print("YES" if ans else "NO")
