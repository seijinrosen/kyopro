from itertools import groupby
from typing import List, Tuple


def run_length_encoding(s: str) -> List[Tuple[str, int]]:
    """ランレングス圧縮"""
    return [(k, len(list(g))) for k, g in groupby(s)]


N = int(input())
S = input()

rl = run_length_encoding(S)
ans = len(rl)

print(ans)
