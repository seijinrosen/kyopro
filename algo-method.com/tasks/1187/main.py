def int2base(number: int, base: int) -> str:
    d = {2: bin, 8: oct, 16: hex}
    if base in d:
        return d[base](number)[2:]
    if number == 0:
        return "0"

    def f(n: int, b: int) -> str:
        if n == 0:
            return ""
        return f(n // b, b) + str(n % b)

    return f(number, base)


N = int(input())
S = input()

ans = int2base(int(S, 2), 16).upper().zfill(N // 4)
print(ans)
