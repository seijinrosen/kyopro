from typing import List

N = int(input())


def func(i: int) -> str:
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    if i % 3 == 0:
        return "Fizz"
    if i % 5 == 0:
        return "Buzz"
    return str(i)


def solve() -> List[str]:
    return list(map(func, range(1, N + 1)))


print(*solve(), sep="\n")
