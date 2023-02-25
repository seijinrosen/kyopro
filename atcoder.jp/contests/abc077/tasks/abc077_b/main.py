from math import floor, sqrt


def is_square_number(n: int) -> bool:
    return sqrt(n).is_integer()


N = int(input())


square_numbers = [
    i**2 for i in range(1, floor(sqrt(N)) + 1) if is_square_number(i**2)
]


print(square_numbers[-1])
