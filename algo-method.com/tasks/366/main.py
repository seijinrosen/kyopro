def sum_of_arithmetic_progression(head: int, last: int, n: int = 0) -> int:
    """等差数列の和"""
    if n == 0:
        # 公差 d = 1 の場合、項数 n は省略可
        n = last - head + 1
    return n * (head + last) // 2


N, *X = map(int, open(0).read().split())


def binary_search(x: int) -> int:
    lo = 1
    hi = x
    while lo < hi:
        mid = (lo + hi) // 2
        if x <= sum_of_arithmetic_progression(1, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


ans = map(binary_search, X)
print(*ans, sep="\n")
