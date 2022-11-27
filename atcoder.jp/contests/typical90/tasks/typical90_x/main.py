from operator import sub


def is_same_parity(x: int, y: int) -> bool:
    return x % 2 == y % 2


N, K = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())

diff_sum = sum(map(abs, map(sub, A, B)))
ans = diff_sum <= K and is_same_parity(diff_sum, K)

print("Yes" if ans else "No")
