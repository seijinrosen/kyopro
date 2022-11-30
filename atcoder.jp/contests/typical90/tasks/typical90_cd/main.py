def sum_of_arithmetic_progression(head: int, last: int, n: int = 0) -> int:
    """等差数列の和"""
    if n == 0:
        # 公差 d = 1 の場合、項数 n は省略可
        n = last - head + 1
    return n * (head + last) // 2


L, R = input().split()
MOD = 10**9 + 7

ans = 0
for i in range(len(L), len(R) + 1):
    l = max(int(L), 10 ** (i - 1))
    r = min(int(R), 10**i - 1)
    ans += sum_of_arithmetic_progression(l, r) % MOD * i
    ans %= MOD

print(ans)
