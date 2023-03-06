# x ページ目に表示されるのは何位から何位までかを返す関数
def paginate(n: int, x: int):
    return n * (x - 1) + 1, n * x


# 標準入力から値を受け取る
# n: int 型
# x: int 型
n = int(input())
x = int(input())

# 答えを求め、出力する
first, last = paginate(n, x)
print(f"{first} ~ {last}")
