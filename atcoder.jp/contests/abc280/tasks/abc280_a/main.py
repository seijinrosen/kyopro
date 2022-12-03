H, W = map(int, input().split())
S = [input() for _ in range(H)]

cnt = 0
for row in S:
    for c in row:
        if c == "#":
            cnt += 1

print(cnt)
