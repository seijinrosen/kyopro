from typing import Counter


def division(a: int, b: int, mod: int) -> int:
    """a ÷ b を mod で割った余り"""
    return a * pow(b, mod - 2, mod) % mod


N, P, *A = map(int, open(0).read().split())

MOD = 10**9 + 7
counter: Counter[int] = Counter()

ans = 0
for i, a in enumerate(A):
    a %= MOD
    ans += i if a == P == 0 else counter[division(P, a, MOD)]
    counter[a] += 1

print(ans)
