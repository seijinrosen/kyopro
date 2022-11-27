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


N, K = input().split()

now = N
for _ in range(int(K)):
    now = int2base(int(now, 8), 9).replace("8", "5")

print(now)
