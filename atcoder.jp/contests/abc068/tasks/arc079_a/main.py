from typing import List, Tuple

N, M = map(int, input().split())
ab: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(M)]


ans = {b for a, b in ab if a == 1} & {a for a, b in ab if b == N}


print("POSSIBLE" if ans else "IMPOSSIBLE")
