X, Y = map(int, input().split())


def prize(n: int) -> int:
    d = {3: 100000, 2: 200000, 1: 300000}
    return d.get(n, 0)


def additional_prize(x: int, y: int) -> int:
    if x == 1 and y == 1:
        return 400000
    return 0


ans = prize(X) + prize(Y) + additional_prize(X, Y)
print(ans)
