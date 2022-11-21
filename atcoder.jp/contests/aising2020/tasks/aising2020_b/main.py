def odd(n: int) -> bool:
    return n % 2 == 1


N = int(input())
A = map(int, input().split())

ans = sum(odd(i) and odd(a) for i, a in enumerate(A, 1))
print(ans)
