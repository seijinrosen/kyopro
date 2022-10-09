from itertools import accumulate


def input_int_pair_list(n: int) -> "list[tuple[int, int]]":
    return [tuple(map(int, input().split())) for _ in range(n)]


D = int(input())
N = int(input())
LR = input_int_pair_list(N)


B = [0] * (D + 1)
for l, r in LR:
    B[l - 1] += 1
    B[r] -= 1

ans = [*accumulate(B)][:D]


print(*ans, sep="\n")
