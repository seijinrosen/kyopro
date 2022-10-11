from typing import Tuple


def input_pair() -> Tuple[str, str]:
    return tuple(input().split())


N, M = map(int, input().split())
FC = [input_pair() for _ in range(N)]
X = input().split()

menu = {f: int(c) for f, c in FC}
ans = sum(menu[x] for x in X)

print(ans)
