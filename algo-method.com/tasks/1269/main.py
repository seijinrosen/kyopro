# 投票先を表す文字列
S = input()

# 1 番目から 5 番目の立候補者への投票数
votes = [0, 0, 0, 0, 0]

for vote in S:
    # i 番目の投票した立候補者
    x = int(vote)
    votes[x - 1] += 1

# 最終的な投票数を答える
print(*votes)
