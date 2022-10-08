def even(n: int) -> bool:
    return n % 2 == 0


H, W, P, Q = map(int, input().split())


ans = "Black" if even(P + Q) else "White"


print(ans)
