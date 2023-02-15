# 標準入力から値を受け取る
# S: str 型
S = input()

# 英単語をキーとし、対応する数字を値とする辞書型の変数
numbers_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
}

ans = numbers_dict[S]


print(ans)
