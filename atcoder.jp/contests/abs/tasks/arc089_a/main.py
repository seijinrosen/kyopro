from typing import Union


def is_same_parity(x: int, y: int) -> bool:
    return x % 2 == y % 2


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


def input_int_tuple_list(n: int) -> "list[tuple[int, int, int]]":
    return [tuple(map(int, input().split())) for _ in range(n)]


def solve(txy: "list[tuple[int, int, int]]") -> bool:
    current_t = 0
    current_x = 0
    current_y = 0
    for t, x, y in txy:
        required_time = t - current_t
        dist = abs(x - current_x) + abs(y - current_y)
        if required_time < dist or not is_same_parity(required_time, dist):
            return False
        current_t = t
        current_x = x
        current_y = y
    return True


def main() -> None:
    N = int(input())
    TXY = input_int_tuple_list(N)

    ans = solve(TXY)

    print(yes_no(ans))


main()
