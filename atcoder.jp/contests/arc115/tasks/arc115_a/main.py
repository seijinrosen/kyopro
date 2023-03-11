def is_even(x: int) -> bool:
    return x % 2 == 0


def is_odd(x: int) -> bool:
    return x % 2 == 1


N, M = map(int, input().split())
S = [input() for _ in range(N)]


answered_1 = [s.count("1") for s in S]
ans = sum(map(is_even, answered_1)) * sum(map(is_odd, answered_1))


print(ans)
