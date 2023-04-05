from math import sqrt


def is_square_number(n: int) -> bool:
    return sqrt(n).is_integer()


a, b = input().split()


ans = is_square_number(int(a + b))


print("Yes" if ans else "No")
