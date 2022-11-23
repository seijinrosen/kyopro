from typing import Iterator, List, Tuple


def neighborhood(i: int, j: int) -> Iterator[Tuple[int, int]]:
    for di, dj in zip((-1, 0, 0, 1), (0, -1, 1, 0)):
        yield i + di, j + dj


H, W = map(int, input().split())
S = [input() for _ in range(H)]
Q = int(input())
XY: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(Q)]

ans = (
    [S[ni][nj] for ni, nj in neighborhood(x, y) if 0 <= ni < H if 0 <= nj < W].count(
        "#"
    )
    for x, y in XY
)

print(*ans, sep="\n")
