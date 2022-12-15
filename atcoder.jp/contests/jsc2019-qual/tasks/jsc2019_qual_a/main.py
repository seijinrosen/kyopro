from itertools import product

M, D = map(int, input().split())


def is_product_day(m: int, d: int) -> bool:
    if d < 10:
        return False
    d10, d1 = map(int, str(d))
    return all([d1 >= 2, d10 >= 2, d1 * d10 == m])


ans = sum(is_product_day(m, d) for m, d in product(range(1, M + 1), range(1, D + 1)))
print(ans)
