# 標準入力から値を受け取る
# diff: int 型
diff = int(input())

# 受け取った値を利用してコードを書いてください
if 1 <= diff <= 9:
    print("easy")
elif 11 <= diff <= 19:
    print("normal")
elif 21 <= diff <= 29:
    print("hard")
else:
    print("special")
