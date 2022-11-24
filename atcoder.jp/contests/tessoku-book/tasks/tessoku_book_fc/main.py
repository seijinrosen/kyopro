def int2bin(number: int, width: int) -> str:
    return bin(number)[2:].zfill(width)


N = int(input())

d = str.maketrans({"0": "4", "1": "7"})
ans = int2bin(N - 1, 10).translate(d)

print(ans)
