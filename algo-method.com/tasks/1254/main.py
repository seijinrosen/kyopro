# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
table = str.maketrans({"o": "x", "x": "o"})
ans = S.translate(table)


print(ans)
