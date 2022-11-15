from typing import Tuple


def input_ab() -> Tuple[int, str]:
    a, b = input().split()
    return int(a), b


N, L = map(int, input().split())
AB = [input_ab() for _ in range(N)]

ans = max(L - a if b == "E" else a for a, b in AB)
print(ans)
