X = int(input())


def f(x: int) -> int:
    if x < 600:
        return 8
    if x < 800:
        return 7
    if x < 1000:
        return 6
    if x < 1200:
        return 5
    if x < 1400:
        return 4
    if x < 1600:
        return 3
    if x < 1800:
        return 2
    return 1


ans = f(X)
print(ans)
