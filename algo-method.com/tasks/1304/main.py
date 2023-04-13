# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
lower_vowels = {"a", "i", "u", "e", "o"}


def convert(ch: str) -> str:
    if ch.islower() and ch not in lower_vowels:
        return "_"
    return ch


ans = "".join(map(convert, S))


print(ans)
