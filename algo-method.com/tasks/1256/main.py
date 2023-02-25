# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
def translate(s: str) -> str:
    table = str.maketrans("abc", "bca")
    return s.translate(table)


T = translate(S)
U = translate(T)
V = translate(U)


print(T)
print(U)
print(V)
