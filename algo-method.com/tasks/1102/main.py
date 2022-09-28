N = int(input())
A = list(map(int, input().split()))

current_max = 0
current_max_cnt = 0
ans: "list[int]" = []

for a in A:
    if a == current_max:
        current_max_cnt += 1
    elif current_max < a:
        current_max = a
        current_max_cnt = 1
    ans.append(current_max_cnt)

print(*ans, sep="\n")
