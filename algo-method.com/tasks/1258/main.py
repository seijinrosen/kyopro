# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
def convert(ch: str) -> str:
    if ch == "a":
        return "x"
    if ch == "b":
        return "y"
    if ch == "c":
        return "z"
    return chr(ord(ch) - 3)


ans = "".join(map(convert, S))


print(ans)
