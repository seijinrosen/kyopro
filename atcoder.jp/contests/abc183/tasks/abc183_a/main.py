def relu(x: int) -> int:
    if x >= 0:
        return x
    return 0


x = int(input())


print(relu(x))
