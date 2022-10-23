S = input()

d = {"6": "9", "9": "6"}
ans = S[::-1].translate(str.maketrans(d))

print(ans)
