from typing import Optional, Tuple

N = int(input())


def solve() -> Optional[Tuple[int, int]]:
    for a in range(1, N):
        aa = 3**a
        if aa >= N:
            break

        for b in range(1, N):
            x = aa + 5**b
            if x == N:
                return a, b
            if x > N:
                break


ans = solve()


if ans is not None:
    print(*ans)
else:
    print(-1)
