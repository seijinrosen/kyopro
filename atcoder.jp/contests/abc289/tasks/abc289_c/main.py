from itertools import product
from typing import Iterator, List, Set, Tuple


def bitset(n: int) -> Iterator[Tuple[int, ...]]:
    """bit 全探索"""
    for bits in product((0, 1), repeat=n):
        yield bits


N, M = map(int, input().split())
S: List[Set[int]] = []
for _ in range(M):
    input()
    S.append(set(map(int, input().split())))


def solve() -> int:
    ans = 0

    for bits in bitset(M):
        st: Set[int] = set()

        for i, b in enumerate(bits):
            if b:
                st.update(S[i])

        if len(st) == N:
            ans += 1

    return ans


print(solve())
