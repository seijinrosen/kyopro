S = input()


d = {
    "Left": "<",
    "Right": ">",
    "AtCoder": "A",
}
ans = map(d.get, S.split())


print(*ans)
