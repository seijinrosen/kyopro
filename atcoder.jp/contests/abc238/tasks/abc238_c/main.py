def sum_of_arithmetic_progression(head: int, last: int, n: int = 0) -> int:
    """等差数列の和"""
    if n == 0:
        # 公差 d = 1 の場合、項数 n は省略可
        n = last - head + 1
    return n * (head + last) // 2


N = int(input())


def head(i: int) -> int:
    return int("1" + "0" * (i - 1))


def last(i: int) -> int:
    return min(N, int("9" * i))


MOD = 998244353
ans = sum(
    sum_of_arithmetic_progression(1, last(i) - head(i) + 1) % MOD
    for i in range(1, len(str(N)) + 1)
)


print(ans % MOD)
