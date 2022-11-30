from itertools import groupby
from typing import List, Tuple


def run_length_encoding(s: str) -> List[Tuple[str, int]]:
    """ランレングス圧縮"""
    return [(k, len(list(g))) for k, g in groupby(s)]


N = int(input())
S = input()

i = 0
ans = 0
for _, cnt in run_length_encoding(S):
    i += cnt
    ans += (i - cnt) * cnt

print(ans)
