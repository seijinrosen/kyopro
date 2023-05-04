from itertools import groupby
from typing import List, Tuple

N = int(input())
S = input()


def run_length_encoding(s: str) -> List[Tuple[str, int]]:
    """ランレングス圧縮"""
    return [(k, len(list(g))) for k, g in groupby(s)]


def solve() -> int:
    run_length = run_length_encoding(S)

    if len(run_length) <= 1:
        return -1

    return max(v for k, v in run_length if k == "o")


print(solve())
