N = int(input())
S = [sum(map(int, input().split())) for _ in range(N)]


def solve() -> int:
    return sum(0 <= s < 20 for s in S)


print(solve())
