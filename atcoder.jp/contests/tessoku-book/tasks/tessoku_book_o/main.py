from typing import Any, List


def coordinate_compression(lst: List[Any], start: int = 0) -> List[int]:
    """座標圧縮
    >>> coordinate_compression([46, 80, 11, 77, 46], start=1)
    [2, 4, 1, 3, 2]
    >>> coordinate_compression([8, 100, 33, 12, 6, 1211])
    [1, 4, 3, 2, 0, 5]
    """
    d = {x: i for i, x in enumerate(sorted(set(lst)), start=start)}
    return [d[x] for x in lst]


N = int(input())
A = list(map(int, input().split()))

ans = coordinate_compression(A, start=1)
print(*ans)
