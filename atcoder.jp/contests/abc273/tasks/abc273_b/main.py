from decimal import ROUND_HALF_UP, Decimal
from functools import reduce


def round_half_up(number: int, ndigits: int) -> int:
    """四捨五入
    参考: https://note.nkmk.me/python-round-decimal-quantize/
    """
    return int(
        Decimal(number).quantize(Decimal(f"1E{-ndigits}"), rounding=ROUND_HALF_UP)
    )


X, K = map(int, input().split())

ans = reduce(lambda x, i: round_half_up(x, -i), range(1, K + 1), X)
print(ans)
