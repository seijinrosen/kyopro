from math import sqrt
from typing import Iterable, List, Tuple


def dist(p: Iterable[float], q: Iterable[float]) -> float:
    # https://docs.python.org/ja/3/library/math.html#math.dist
    return sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))


txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())
xy: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(n)]


ans = min(dist((txa, tya), house) + dist(house, (txb, tyb)) for house in xy) <= T * V


print("YES" if ans else "NO")
