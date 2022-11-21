def odd(n: int) -> bool:
    return n % 2 == 1


N, *A = map(int, open(0).read().split())

ans = sum(map(odd, A[::2]))
print(ans)
