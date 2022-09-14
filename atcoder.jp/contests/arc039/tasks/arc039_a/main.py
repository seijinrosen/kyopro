A, B = input().split()


def max_A(a: str) -> int:
    if a[0] != "9":
        return int("9" + a[1] + a[2])
    if a[1] != "9":
        return int(a[0] + "9" + a[2])
    return int(a[0] + a[1] + "9")


def min_B(b: str) -> int:
    if b[0] != "1":
        return int("1" + b[1] + b[2])
    if b[1] != "0":
        return int(b[0] + "0" + b[2])
    return int(b[0] + b[1] + "0")


ans = max(max_A(A) - int(B), int(A) - min_B(B))
print(ans)
