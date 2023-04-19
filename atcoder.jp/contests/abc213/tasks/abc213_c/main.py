from typing import Any, List, Tuple


def coordinate_compression(lst: List[Any], start: int = 0) -> List[int]:
    d = {x: i for i, x in enumerate(sorted(set(lst)), start=start)}
    return [d[x] for x in lst]


H, W, N = map(int, input().split())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]


ans = zip(
    coordinate_compression([a for a, _ in AB], 1),
    coordinate_compression([b for _, b in AB], 1),
)


for row in ans:
    print(*row)
